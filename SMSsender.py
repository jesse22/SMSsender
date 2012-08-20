#! /usr/bin/env python
import smtplib
import wx

class MainWindow(wx.Frame):
  def __init__(self,parent,id):

    global number
    global selection
    ATT = "@txt.att.net"
    TMobile = "@tmomail.net"
    Sprint = "@messaging.sprintpcs.com"
    Verizon = "@vtext.com"
    Virgin = "@vmobl.com"
    Pick = "Pick One"
    wx.Frame.__init__(self,parent,id,'Frame aka window', size=(300,200))
    self.Show(True)
    panel = wx.Panel(self)
    #carrier list
    carriers = [Pick, ATT, TMobile, Sprint, Verizon, Virgin]

    user = wx.TextEntryDialog(self, "Login", "Username", "")
    
    if user.ShowModal() == wx.ID_OK:
      username=user.GetValue()
      password = wx.TextEntryDialog(self, "Password", "Password", "")
      if password.ShowModal() == wx.ID_OK:
        pwd =password.GetValue()
	phone_number = wx.TextEntryDialog(self,"Phone Number", "Phone Number", "")
	if phone_number.ShowModal() == wx.ID_OK:
	  number = phone_number.GetValue()
	  self.carrier = wx.SingleChoiceDialog(self, "Select the carrier of your friend", "The Carrier", carriers, wx.CHOICEDLG_STYLE)
	  self.carrier.Bind(wx.EVT_COMBOBOX, self.onCombo)
	  if self.carrier.ShowModal() == wx.ID_OK:
	    carrier1 = self.carrier.GetStringSelection()
	    email = number + carrier1
	    message = wx.TextEntryDialog(self,"Your Message", "Your Message", "")
	    if message.ShowModal() == wx.ID_OK:
	  
	      msg = message.GetValue()
              smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
              smtpserver.ehlo()
              smtpserver.starttls()
              smtpserver.ehlo
              smtpserver.login(username, pwd)
              header = 'To:' + email + '\n' + 'From: ' + username + '\n' + 'Subject:testing \n'
              print header
              msg1 = header + msg
              smtpserver.sendmail(username, email, msg1)
              smtpserver.close()

  def onCombo(self, event):
    

    self.selection = self.carrier.GetValue()
    print self.selection
    print self.number
    self.email = number + selection
    print email
    return self.email


  def OnClose(self, event):
    self.close()
  #def OnSelect(self, event):


if __name__ =='__main__':
  global email
  app=wx.PySimpleApp()
  frame=MainWindow(parent=None, id=-1)
  frame.Show()
  app.MainLoop()


