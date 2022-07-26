s=5;
print(type(s))
s="vikash";
print(type(s))
print(s);
x=1 # int
y=2.8 #float
z=1j #complex

print(type(x))
print(type(y))
print(type(z))

# casting

x1=int(1)
y1=int(2.8)
z1=int("3")

print(type(x1))
print(type(y1))
print(type(z1))
print(y1)

a="asdasd"

b="""What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"""

print(b)
a="Vikash Verma"
print(a[2:5])
print(a[2])
print(a[:5])
print(a[2:])
print(a.upper())
print(a.lower())
b="          vikash               "
print(b)
print(b.strip())
c1="vikash " +"verma is a boy"
print(c1)
age=45;
item=778;
txt="my name age is {} and can be {}"
print(txt.format(age,item))