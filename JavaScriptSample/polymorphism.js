function person(name){
    this.name = name
    this.IntroduceMyself = function(){
        print "I'm " + this.name
    }
}
a = new person("a")
b = new person("b")
b.age = 15
b.IntroduceMyself = function(){
    print "I'm " + this.name + 
        "\nI'm " + this.age + " now."
}
a.IntroduceMyself()
print ""
b.IntroduceMyself()