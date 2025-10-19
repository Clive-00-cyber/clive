#include <iostream>
#include <vector>
#include <cctype>
using namespace std;

struct Question {
    string text;
    vector<string> options;
    char correct;
};

int main() {
    vector<Question> quiz = {
        {"What is the capital of France?", {"A. London", "B. Paris", "C. Berlin"}, 'B'},
        {"2 + 2 * 2 = ?", {"A. 6", "B. 8", "C. 4"}, 'A'},
        {"Which is a vowel?", {"A. B", "B. E", "C. Z"}, 'B'}
    };

    int score = 0;
    char answer;

    cout << "=== Quiz Game ===\n";
    for(int i=0; i<quiz.size(); i++) {
        cout << "\nQuestion " << i+1 << ": " << quiz[i].text << "\n";
        for(string opt : quiz[i].options) cout << opt << "\n";
       
        cout << "Your answer (A/B/C): ";
        cin >> answer;
        answer = toupper(answer);
       
        if(answer == quiz[i].correct) {
            cout << "Correct!\n";
            score++;
        } else {
            cout << "Wrong! Correct answer: " << quiz[i].correct << "\n";
        }
    }

    cout << "\nFinal Score: " << score << "/" << quiz.size() << endl;
    return 0;
}