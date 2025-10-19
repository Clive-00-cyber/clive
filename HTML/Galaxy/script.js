    (function(){
        const canvas = document.getElementById('canvas');
        const gl = canvas.getContext('webgl');
        if (!gl) {
            console.error('WebGL non supporté');
            return;
        }

        const vsSource = `
            attribute vec2 a_position;
            void main() {
                gl_Position = vec4(a_position, 0.0, 1.0);
            }
        `;

        const fsSource = `
            precision mediump float;
            void main() {
                gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); // solid red
            }
        `;

        //
        function createShader(gl, type, source){
            const shader = gl.createShader(type);
            gl.shaderSource(shader, source);
            gl.compileShader(shader);
            if(!gl.getShaderParameter(shader, gl.COMPILE_STATUS)){
                console.error('shader compile failed with: ' +gl.getShaderInfoLog(shader));
            gl.deleteShader(shader);
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
            gl.deleteProgram(program);
                return null;
            }
            return program;
        }

        const program = createProgram(gl, vsSource, fsSource);
        gl.useProgram(program);

        //
        const positionLocation = gl.getAttribLocation(program, 'a_position');

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
            gl.clear(gl.COLOR_BUFFER_BIT);
            gl.drawArrays(gl.TRIANGLES, 0, 6);
            console.log('Render frame');
            requestAnimationFrame(render);
        }
        requestAnimationFrame(render);

    });