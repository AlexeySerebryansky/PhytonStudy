from turtle import *

fillcolor("blue")

begin_fill()
for i in range(4):
    forward(500)
    left(900)
end_fill()

fillcolor("yellow")
begin_fill()
for i in range(4):
    forward(500)
    right(900)
end_fill()

mainloop()
