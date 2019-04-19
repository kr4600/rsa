#!/usr/bin/python

# simple2.py

import wx

app = wx.App()

frame = wx.Frame(None, -1, '')
frame.SetToolTip(wx.ToolTip('This is a frame'))
frame.SetCursor(wx.StockCursor(wx.CURSOR_MAGNIFIER))
frame.SetPosition(wx.Point(0,0))
frame.SetSize(wx.Size(300,250))
frame.SetTitle('simple2.py')
frame.Show()

app.MainLoop()
