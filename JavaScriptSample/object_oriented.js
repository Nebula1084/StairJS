a = {
    i : "This is i",
    f : function (){
        print "This is f"
    },
    1 : 1.0,
    1.4 : 1.4
}


function person(){
    this.name = "Tom"
    this.age = 3
    this.talk = function (){
        print "I'm " + this.name + "."
        print "I'm " + this.age + " now."
    }
    this.grow = function (){
        this.age += 1
    }
}