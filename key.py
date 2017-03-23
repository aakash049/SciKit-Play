def hook():
    import win32com.client as comctl
    wsh = comctl.Dispatch("WScript.Shell")
    wsh.SendKeys("{F11}")
pass