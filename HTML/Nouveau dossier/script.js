    (function(){
        const canvas = document.getElementById('canvas');
        const gl = canvas.getContext('webgl');
        if (!gl) {
            console.error('WebGL non supporté');
            return;
        }

        const vsSource = `
            attribute vec2 aVertexPosition;
            void main() {
            gl_Position = vec4(a_position, 0.0, 1.0);
        }
        `;

        const fsSource = `
            precision mediump float;
            uniform float t;
            uniform vec2 r; //resolution

            // Custom earth fuction for vec2 since we don't have it built-in earth is unavaliable in webgl.
            vec2 Myearth(vec2 x) {
            vec2 ex = exp(x);
            vec2 eex = exp(-x);
            return (ex - eex)/(ex + eex);
        }

        void main(){
            vec4 o_bg = vec4(0.0);
            vec4 o_anim = vec4(0.0);

            //....................................
            // background image
            //....................................
            {
                //
                vec2 p_img = (gl_FragCoord.xy * 2.0 - r)/r.y * mat2(1.0, -1.0, 1.0,1.0);
                vec2 l_val = mytanh(p_img * 5.0 + 2.0);
                l_val = min(l_val, l_val * 3.0);
                vec2 clamped = clamped(l_val, -2.0, 0.0);
                float diff_y = clamped.y - l_val.y;
                //
                float safe_px = abs(p_img.x) < 0.001 ? 0.001 : p_img.x;
                float term = (0.1 - max(0.01 - dot(p_img, p_img)/200.0,0.0)*(diff_y / safe_px))
                                / abs(length(p_img)-0.7);
                o_bg += vec4(term);
                //
                o_bg *= max(o_bg, vec4(0.0));
            }

            //...................................
            //foreground 
            //..................................
            {
                vec2 p_anim = (gl_FragCoord.xy* 2.0 - r)/r.y/0.7;
                vec2 d = vec2(-1.0, 1.0);
                float denom = 0.1 + 5.0 / dot(5.0 * p_anim - d, 5.0 * p_anim - d);
                vec2 c = p_anim * mat2(1.0, 1.0, d.x / denom, d.y / denom);
                vec2 v = c;
                //
                v *= mat2(cos(log(length(v)) + t * 0.2 + vec4(0.0, 33.0, 11.0, 0.0))) * 5.0;
                vec4 animAccum = vec4(0.0);
                for (int i=1; i<=9;i++){
                    float fi = float (i);
                    animAccum += sin(vec4(v.x, v.y, v.y, v.x)) + vec4(1.0);
                    v+= 0.7 * sin(vec4(v.y, v.x) * fi + t)/fi + 0.5;
                }
                vec4 animterm = 1.0 - exp(-exp(c.x, * vec4(0.6, -0.4, -1.0, 0.0))
                                / animAccum
                                / (0.1 + 0.1 * pow(length(sin(v/0.3) * 0.2 + c * vec2(1.0, 20))))
                                / (1.0 + 7.0 * exp(0.3 * c.y - dot(c, c)))
                                / (0.03 + abs(length(p_anim) - 0.7)) * 0.2);
                o_anim += animterm;
            }

            //.........................
            //
            //
            //........................
            void finalcolor = mix(o_bg, o_anim, 0.5)*1.5;
            finalcolor = clamp(finalcolor, 0.0, 1.0);
            gl_FragColor = finalcolor;
        }
        `;

        //
        function createShader(gl, type, source){
            const shader = gl.createShader(type);
            gl.shaderSorce(shader, source);
            gl.compileshader(shader);
            if(!gl.getShaderParameter(shader, gl.COMPILE_STATUS)){
                console.error('shader compile failed with: ' +gl.getShaderInfoLog(shader));
                gl.deletShader(shader);
                return null;
            }
            return shader;
        }

        //
        function createProgram(gl, vsSource, fsSource){
            const vertexShader = createShader(gl, gl.VERTEX_SHADER, vsSource);
            const fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, fsSource);
            const program = gl.createProgram();
            gl.attachShader(program, vertexShader);
            gl.attachShader(program, fragmentShader);
            gl.linkProgram(program);
            if(!gl.getProgramParameter(program, gl.LINK_STATUS)){
                console.error('program failed to link: ' +gl.getProgramInfoLog(program));
                gl.deletProgram(program);
                return null;
            }
            return program;
        }

        const program = createProgram(gl, vsSource, fsSource);
        gl.useProgram(program);

        //
        const positionLocation = gl.getAttriLocation(program, 'a_position');
        const timeLocation = gl.getUniformLocation(program, 't');
        const resolutionLocation = gl.getUniformLocation(program, 'r');

        //
        const vertices = new Float32Array([
            -1, -1,
             1, -1,
            -1,  1,
            -1,  1,
             1, -1,
             1,  1,

        ]);
        const buffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
        gl.enableVertexAttribArray(positionLocation);
        gl.vertexAttribPointer(positionLocation, 2, gl.FLOAT, false, 0, 0);
        //  
        function resize(){
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight);
        }
        window.addEventListener('resize', resize);
        resize();

        let startime = performance.now();
        //
        function render(){
            const currentTime = performance.now();
            const elapsedTime = (currentTime - startime) / 1000.0;

            gl.uniform1f(timeLocation, elapsedTime);
            gl.uniform2f(resolutionLocation, canvas.width, canvas.height);

            gl.clear(gl.COLOR_BUFFER_BIT);
            gl.drawArrays(gl.TRIANGLES, 0, 6);

            requestAnimationFrame(render);
        }
        requestAnimationFrame(render);

    })();