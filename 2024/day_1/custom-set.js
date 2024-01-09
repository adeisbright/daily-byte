/**
 * CustomSet
 * Properties
 * ============
 * setType - To hold the type of values stored in the set 
 * setSize - To hold the size of the set 
 * set - An instance property that refers to the data within our set 
 * Methods
 * ======== 
 * add(value) - Add an item to the set 
 * show() -  Display the items we have within our set 
 * has(value) -> Returns true if the value is in our custom set 
 * remove(value)
 */

class CustomSet {
    setType = null 
    setSize = 0
    constructor(){
        this.set = {}
        this.iterator = this.generateValues()
    }
    add(value){
        if (this.setSize && this.setType){
            if(typeof value !== this.setType){
                throw new Error(`BadTypeError: ${value} should be of type ${this.setType}`)
            }
        }
        if(!this.has(value)){
            this.set[value] = value
            this.setSize += 1
        }
        if(!this.setType){
            this.setType = typeof value 
        }
        return this.set
    }
    has(value){
        const hasValue = this.set[value] ? true  : false 
        return  hasValue
    }
    show(){
        for (let value of this.generateValues()){
           console.log(value)
        }
    }
    *generateValues(){
        for (let key of Object.keys(this.set)){
            if(this.set.hasOwnProperty(key)){
               yield key
            }
        }
    }
    nextValue(){
        return this.iterator.next().value
    }
}

const mySet = new CustomSet() 
mySet.add(4) 
mySet.add(3)
mySet.add(5)
mySet.add(5)
mySet.add(5)
//mySet.show()
console.log(mySet.nextValue())
console.log(mySet.nextValue()) 
console.log(mySet.nextValue())
console.log(mySet.nextValue())