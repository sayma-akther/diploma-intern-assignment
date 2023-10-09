def my_name_is():
    print("My name is Sayma Akther")


def i_have_enrolled_course(course_name):
     print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"



course_and_learn = [
    {
        "course": "Python and Web",
        "frontend": "HTML,CSS,JavaScripts",
        "backend": "Python"

    },
    {
        "course": "Java Spring Boot",
        "frontend": "HTML,CSS,Hibernet",
        "backend": "Java"

    },
    {
        "course": "C# & ASP.NET Core",
        "frontend": "Entity Framework, Razor",
        "backend": "C#"

    },
    {
        "course": "MERN Development",
        "frontend": "React, HTML, CSS",
        "backend": "Node"

    },
    {
        "course": "PHP & Laravel",
        "frontend": "HTML,CSS,Blade, Eloquent",
        "backend":"PHP , Artisan CLI"

    }
]


for item in course_and_learn:
    # print(item)
    course_name =  item["course"]
    backend = item["backend"] 
    frontend = item["frontend"]
    
    my_name_is()  
    i_have_enrolled_course(course_name)
    result =  i_have_learning(backend, frontend)
    print(result)
    print()
# Update the code according your name, and different types of course listed in Bangla Fighter Website: https://banglafighter.com/crs
