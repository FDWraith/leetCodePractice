/*
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
*/

const isNumber = (n) => !isNaN(n);

class MyHashSet {
    constructor() {
        this.count = 0;
        this.size = 10;
        this.storage = new Array(this.size);
    }

    _grow() {
        const oldStorage = this.storage;
        this.size = this.size * 2;
        this.storage = new Array(this.size);
        this.count = 0;

        oldStorage.forEach(item => {
            if (isNumber(item)) {
                this.add(item);
            } else if (item instanceof Array) {
                this.addAll(item);
            }
        })
    }

    /**
     * @param {array} keys 
     * @return {void}
     */
    addAll(keys) {
        keys.forEach(key => {
            this.add(key);
        })
    }

    /** 
     * @param {number} key
     * @return {void}
     */
    add(key) {
        if (this.count > this.size * 0.75) {
            this._grow();
        }

        if (this.contains(key)) {
            return;
        }

        const index = key % this.size;
        let exists;
        if (exists = this.storage[index]) {
            if (isNumber(exists)) {
                const arr = [exists];
                this.storage[index] = arr;
            }
            this.storage[index].push(key);
        } else {
            this.storage[index] = key;
        }
        this.count += 1;
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        if (!this.contains(key)) {
            return;
        }

        const index = key % this.size;
        const item = this.storage[index];
        if (isNumber(item)) {
            this.storage[index] = null;
        } else if (item instanceof Array) {
            const pivot = item.indexOf(key);
            this.storage[index] = item.slice(0, pivot).concat(item.slice(pivot + 1));
        }
        this.count -= 1;
    }

    /**
     * Returns true if this set contains the specified element
     * @param {number} key
     * @return {boolean}
     */
    contains(key) {
        const index = key % this.size;
        const item = this.storage[index];
        return key === item || (item instanceof Array && item.includes(key));
    }
}

let hashSet = new MyHashSet();
hashSet.add(1);
console.log(hashSet.contains(0)); // expects false
console.log(hashSet.contains(1)); // expects true
hashSet.remove(1);
hashSet.add(11);
console.log(hashSet.contains(1)); // expects false
console.log(hashSet.contains(11)); // expects true
hashSet.add(1);
hashSet.remove(11);
console.log(hashSet.contains(1)); // expects true
console.log(hashSet.contains(11)); //expects false
hashSet.remove(1);
hashSet.remove(11);
hashSet.remove(1);
hashSet.add(2);
console.log(hashSet.contains(1)); //expects false
hashSet.add(1);
hashSet.add(1);
hashSet.add(1);
hashSet.remove(1);
console.log(hashSet.contains(1)); //expects false
hashSet.add(20);
hashSet.add(10);
hashSet.add(11);
console.log(hashSet.contains(20)); //expects true
hashSet.add(30);
hashSet.remove(10);
console.log(hashSet.contains(20)); //expects true
console.log(hashSet.storage);


/*
*/