/*
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
*/

class WordDictionary {
    constructor() {
        this.isWord = false;
        this.children = {};
    }

    addWord(word) {
        if (word === '') {
            this.isWord = true;
            return;
        }

        const first = word.charAt(0);
        let child = this.children[first];
        if (!child) {
            child = this.children[first] = new WordDictionary(); 
        }
        child.addWord(word.slice(1));
    }

    search(word) {
        if (word === '') {
            return this.isWord;
        }

        const first = word.charAt(0);
        if (first === '.') {
            return Object.values(this.children).some(child => child.search(word.slice(1)));
        }
        return this.children[first] !== undefined && this.children[first].search(word.slice(1));
    }
}

const wd = new WordDictionary();
wd.addWord('hello');
wd.addWord('me');
console.log(wd.search('h')); // expects true
console.log(wd.search('helloooo')); // epxects false
console.log(wd.search('he..o')); // expects true
console.log(wd.search('.....')); // expects true;
console.log(wd.search('.........')) // expects false
console.log(wd.search('.e')); // expects true
console.log(wd.search('.me')); //expects false

wd.addWord('at');
wd.addWord('and');
wd.addWord('an');
wd.addWord('add');
console.log(wd.search('a'));