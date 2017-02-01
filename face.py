# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:11:12 2016

@author: luzhangqin
"""
 
import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import exit
#向sys模块借一个exit函数用来退出程序

import Image

import numpy
import matplotlib.pyplot
import matplotlib.colors
from skimage import io,data


filename = 'face.jpg'

#指定图像文件名称
def zh_rgb(x, y, filename):
    pix_list = []
    r_list=[]
    g_list=[]
    b_list=[]
    r_var = g_var = b_var = 0
    r_mean = g_mean = b_mean = 0
    eucl_dis = 0
    chess_dis = 0
    
    eucl_dis_pic = Image.new('RGB', (216, 288))
    chess_dis_pic = Image.new('RGB', (216, 288))    
    
    image = Image.open(filename,'r')
    for i_pix in range(x-2, x+3):
        for j_pix in range(y-2, y+3):
            pix = image.getpixel((i_pix, j_pix))
            pix_list.append(pix)
            r_list.append(pix[0])
            g_list.append(pix[1])
            b_list.append(pix[2])
    #fc        
    r_var = numpy.var(r_list)
    g_var = numpy.var(g_list)
    b_var = numpy.var(b_list)
    rgb_var = r_var+g_var+b_var
    print 'rgb_var%s:'%rgb_var
    
    
    #jz
    r_mean = numpy.mean(r_list)
    g_mean = numpy.mean(g_list)
    b_mean = numpy.mean(b_list)
    print 'r_mean:%s'%r_mean
    print 'g_mean:%s'%g_mean
    print 'b_mean:%s'%b_mean
    
    #bl
    img = io.imread(filename)
    for x_img in range(len(img)):
        for y_img in range(len(img[0])):
                eucl_dis = ((img[x_img][y_img][0] - r_mean)**2 + (img[x_img][y_img][1] - g_mean)**2 + (img[x_img][y_img][1] - g_mean)**2)**0.5
                chess_dis = max(abs(img[x_img][y_img][0] - r_mean),abs(img[x_img][y_img][1] - g_mean),abs(img[x_img][y_img][1] - g_mean))
                if eucl_dis > rgb_var:
                    eucl_dis_pic.putpixel((y_img,x_img),(0,0,0))
                else:
                    eucl_dis_pic.putpixel((y_img,x_img),tuple(img[x_img][y_img]))
                
                if chess_dis > rgb_var:
                    chess_dis_pic.putpixel((y_img,x_img),(0,0,0))
                else:
                    chess_dis_pic.putpixel((y_img,x_img),tuple(img[x_img][y_img]))
    eucl_dis_pic.show()
    chess_dis_pic.show()



def zh_hsv(x,y,filename):
    h_list=[]
    s_list=[]
    v_list=[]
    h_var = s_var = v_var = 0
    h_mean = s_mean = v_mean = 0
    eucl_dis = 0
    chess_dis = 0

    eucl_dis_pic = Image.new('HSV', (216, 288))
    chess_dis_pic = Image.new('HSV', (216, 288))    
    
    image = matplotlib.pyplot.imread(filename,'r')
    arr = numpy.array(image)
    image_hsv = matplotlib.colors.rgb_to_hsv(arr)
    
    for i_pix in range(x-2, x+3):
        for j_pix in range(y-2, y+3):
            pix = image_hsv[j_pix, i_pix]
            h_list.append(pix[0])
            s_list.append(pix[1])
            v_list.append(pix[2])
    
     #fc        
    h_var = numpy.var(h_list)
    s_var = numpy.var(s_list)
    v_var = numpy.var(v_list)
    hsv_var = h_var+s_var+v_var
    print 'hsv_var%s:'%hsv_var
    
    
    #jz
    h_mean = numpy.mean(h_list)
    s_mean = numpy.mean(s_list)
    v_mean = numpy.mean(v_list)
    print 'h_mean:%s'%h_mean
    print 's_mean:%s'%s_mean
    print 'v_mean:%s'%v_mean

    for x_img in range(len(image_hsv)):
        for y_img in range(len(image_hsv[0])):
                eucl_dis = ((image_hsv[x_img][y_img][0] - h_mean)**2 + (image_hsv[x_img][y_img][1] - s_mean)**2 + (image_hsv[x_img][y_img][2] - v_mean)**2)**0.5
                chess_dis = max(abs(image_hsv[x_img][y_img][0] - h_mean),abs(image_hsv[x_img][y_img][1] - s_mean),abs(image_hsv[x_img][y_img][1] - v_mean))
                if eucl_dis > hsv_var:
                    eucl_dis_pic.putpixel((y_img,x_img),(0,0,0))
                else:
                    eucl_dis_pic.putpixel((y_img,x_img),tuple(image_hsv[x_img][y_img]))
                
                if chess_dis > hsv_var:
                    chess_dis_pic.putpixel((y_img,x_img),(0,0,0))
                else:
                    chess_dis_pic.putpixel((y_img,x_img),tuple(image_hsv[x_img][y_img]))
    eucl_dis_pic.show()
    chess_dis_pic.show()
    
			
pygame.init()
#初始化pygame,为使用硬件做准备
 
screen = pygame.display.set_mode((216, 288), 0, 32)
#创建了一个窗口
pygame.display.set_caption("Hello, World!")
#设置窗口标题
 
background = pygame.image.load(filename).convert()
#加载并转换图像

while True:
#游戏主循环
 
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
        if event.type == MOUSEBUTTONDOWN:
            #接收到退出事件后退出程序
            x,y = pygame.mouse.get_pos()
            zh_rgb(x, y, filename)
            zh_hsv(x, y, filename)
    screen.blit(background, (0,0))
    #将背景图画上去
    pygame.display.update()
    #刷新一下画面
    
