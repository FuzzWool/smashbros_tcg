#SingleInstance force

ResizeWin(Width = 0,Height = 0)
{
  WinGetPos,X,Y,W,H,A
  If %Width% = 0
    Width := W

  If %Height% = 0
    Height := H

  WinMove,A,,%X%,%Y%,%Width%,%Height%
}


Insert::

Run, %windir%\system32\cmd.exe /k "test1.py"
WinWait H:\WINDOWS\system32\cmd.exe
WinMove A,, 0, 0

WinWait Super Smash Bros
ResizeWin(600, 450)
WinMove A,, 650, 0

Run, %windir%\system32\cmd.exe /k "test1.py"
WinWait H:\WINDOWS\system32\cmd.exe
WinMove A,, 0, 500

Sleep, 2000
ResizeWin(600, 450)
WinMove A,, 650, 500