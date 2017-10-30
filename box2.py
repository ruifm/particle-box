# -*- coding: utf-8 -*-
from visual.controls import *
import math
import random
scene.autoscale=0
scene.width=1680
scene.height=1050

#constantes
dt=0.01
g=9.8
h=input("insert height: ")
scene.center=(0,h,0)
scene.range=(4*h,4*h,4*h)
r=input("insert ball radius: ")
scale=0.05
n=0
n2=0
results='Number of red ball collisions is: '
results2='Number of cyan ball collisions is: '
results3='Red ball speed: '
results4='Cyan ball speed:'
motion=True

#objects
ball=sphere(pos=(random.uniform(-h+r,h-r),random.uniform(r,h-r),random.uniform(-h+r,h-r)),radius=r, color=color.red, opacity=0.8, make_trail=True, retain=250)
ball2=sphere(pos=(random.uniform(-h+r,h-r),random.uniform(r,h-r),random.uniform(-h+r,h-r)), radius=r, color=color.cyan, opcaity=0.6, make_trail=True, retain=250)
wall1=box(pos=(-h-0.05,h,0.), size=(0.1,2*h,2*h), color=color.green)
wall2=box(pos=(h+0.05,h,0.), size=(0.1,2*h,2*h), color=wall1.color)
wall3=box(pos=(0.,h,-h-0.05), size=(2*h,2*h,0.1), color=color.blue)
floor=box(pos=(0.,-0.05,0.), size=(2*h,0.1,2*h), color=color.white)
ceiling=box(pos=(0.,0.05+2*h,0.), size=(2*h,0.1,2*h), color=floor.color)
front=box(pos=(0.,h,h+0.05), size=(2*h,2*h,0.1), color=color.orange, opacity=0.2)
ball.e=1
ball2.e=1
ball.vel=vector(random.uniform(-2*h,2*h),random.uniform(-2*h,2*h),random.uniform(-2*h,2*h))
ball2.vel=vector(random.uniform(-2*h,2*h),random.uniform(-2*h,2*h),random.uniform(-2*h,2*h))
pointer=arrow(pos=ball.pos, axis=ball.vel*scale, color=color.orange)
pointer2=arrow(pos=ball2.pos, axis=ball2.vel*scale, color=color.orange)
collisions=label(pos=(-2*h,2*h,0), text=results, color=color.white, opacity=0)
collisions2=label(pos=(2*h,2*h,0), text=results2, color=color.white, opacity=0)
collisions3=label(pos=(-2*h,2*h-15,0), text=results3, color=color.white, opacity=0)
collisions4=label(pos=(2*h,2*h-15,0), text=results4, color=color.white, opacity=0)
#controls
c=controls(x=30,y=0, width=300, height=300, range=60, title="reset & e setting")

def setPos():
    ball.pos=(random.uniform(-h+r,h-r),random.uniform(r,h-r),random.uniform(-h+r,h-r))
    ball2.pos=(random.uniform(-h+r,h-r),random.uniform(r,h-r),random.uniform(-h+r,h-r))
    ball.vel=vector(random.uniform(-2*h,2*h),random.uniform(-2*h,2*h),random.uniform(-2*h,2*h))
    ball2.vel=vector(random.uniform(-2*h,2*h),random.uniform(-2*h,2*h),random.uniform(-2*h,2*h))
    motion=True
    n=0
    n2=0
b=button(pos=(25,0),width=25, length=100, text="RESET", action=lambda: setPos(), color=color.red)
def setE(s):
    ball.e=s.value
    ball2.e=s.value
s=slider(pos=(-30,40), width=10, length=70, axis=(1,0,0), min=0, max=1, action=lambda: setE(s), color=color.green, title="E setting")
s.value=1

#motion
while motion:
    rate(100)
    d = sqrt((ball.pos.x-ball2.pos.x)**2 + (ball.pos.y-ball2.pos.y)**2 + (ball.pos.z-ball2.pos.z)**2)
    ball.color=color.red
    wall1.color=color.green
    wall2.color=color.green
    wall3.color=color.blue
    ceiling.color=color.white
    floor.color=color.white
    front.color=color.orange
    pointer.pos=ball.pos
    pointer.axis=ball.vel*scale
    pointer2.pos=ball2.pos
    pointer2.axis=ball2.vel*scale
    ball.pos=ball.pos+ball.vel*dt
    if floor.pos.y + ball.radius < ball.pos.y < ceiling.pos.y - ball.radius:
        ball.vel.y=ball.vel.y-g*dt
    if floor.pos.y + ball2.radius < ball2.pos.y < ceiling.pos.y - ball.radius:
        ball2.vel.y=ball2.vel.y-g*dt
    if ball.pos.y <= floor.pos.y + ball.radius:
        n=n+1
        ball.vel.y=-ball.vel.y*ball.e
        ball.color=color.black
        floor.color=color.blue
    if ball.pos.x >= wall2.pos.x - ball.radius:
        n=n+1
        ball.color=color.black
        wall2.color=color.red
        ball.vel.x=-ball.vel.x*ball.e
    if ball.pos.x <= wall1.pos.x + ball.radius:
        n=n+1
        ball.vel.x=-ball.vel.x*ball.e
        ball.color=color.black
        wall1.color=color.red
    if ball.pos.y >= ceiling.pos.y - ball.radius:
        n=n+1
        ball.vel.y=-ball.vel.y*ball.e
        ball.color=color.black
        ceiling.color=color.orange
    if ball.pos.z <= wall3.pos.z + ball.radius:
        n=n+1
        ball.vel.z=-ball.vel.z*ball.e
        ball.color=color.black
        wall3.color=color.white
    if ball.pos.z >= front.pos.z - ball.radius:
        n=n+1
        ball.vel.z=-ball.vel.z*ball.e
        ball.color=color.black
        front.color=color.green
    if ball.vel == (0.,0.,0.):
        motion=False
    ball2.pos = ball2.pos + ball2.vel*dt
    if ball2.pos.y <= floor.pos.y + ball2.radius:
        n2=n2+1
        ball2.vel.y=-ball2.vel.y*ball2.e
    if ball2.pos.x >= wall2.pos.x - ball2.radius:
        n2=n2+1
        ball2.vel.x=-ball2.vel.x*ball2.e
    if ball2.pos.x <= wall1.pos.x + ball2.radius:
        n2=n2+1
        ball2.vel.x=-ball2.vel.x*ball2.e
    if ball2.pos.y >= ceiling.pos.y - ball2.radius:
        n2=n2+1
        ball2.vel.y=-ball2.vel.y*ball2.e
    if ball2.pos.z <= wall3.pos.z + ball2.radius:
        n2=n2+1
        ball2.vel.z=-ball2.vel.z*ball2.e
    if ball2.pos.z >= front.pos.z - ball2.radius:
        n2=n2+1
        ball2.vel.z=-ball2.vel.z*ball2.e
    if ball2.vel == (0.,0.,0.):
        motion=False
    collisions.text=results + str(n)
    collisions2.text=results2 + str(n2)
    collisions3.text=results3 + str(sqrt(ball.vel.x**2+ball.vel.y**2+ball.vel.z**2))
    collisions4.text=results4 + str(sqrt(ball2.vel.x**2+ball2.vel.y**2+ball2.vel.z**2))
    

    

