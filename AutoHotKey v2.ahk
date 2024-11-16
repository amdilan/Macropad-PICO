
; #=WIN , !=ALT, ^=CTRL, +=SHIFT, &=BOTHKEYS(Up AND NumpadUP), ;=COMMENTS
; > =Right < =Left

; Runs only one instance
#SingleInstance Force

; Add the HotKeys that doesn't need ScrollLock ON
#RControl::Send "{AppsKey}"
~!RButton::Send "{AppsKey}"
>!F6::Send "Volume_Mute"
>!F7::Send "Volume_Down"
>!F8::Send "Volume_Up"
>!F9::Send "Media_Prev"
>!F10::Send "Media_Play_Pause"
>!F11::Send "Media_Next"
;
; Open MPC
>!1::Run "<DIR>\MPC-HC\mpc-hc64.exe"
;
; Open Windows Explorer
>!2::Run "C:\Windows\explorer.exe"
;
; Open Spotify
>!3::Run "<DIR\Spotify.lnk"
;
; Macropad buttons
F13::{
	Result := MsgBox("Recycle Bin Warning","Empty the Recycle Bin?","OC")
	If result = "Ok" {
		FileRecycleEmpty
	}
}
<+F13::Run "::{645FF040-5081-101B-9F08-00AA002F954E}" ; RecycleBin Folder
F14::Run "<DIR>\MPC-HC\mpc-hc64.exe"
F15::Run "<DIR>\Spotify.lnk"
F16::Run "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
F17::Run "<DIR>\Everything\Everything.exe"
F18::Run "notepad.exe"
F19::Run "<DIR>\AutoHotkey\WinStoreAppLinks\Terminal.lnk"
<+F19::Run "*RunAs <DIR>\AutoHotkey\WinStoreAppLinks\Terminal.lnk"
F20::Run "calc.exe"
F21::Run "<DIR>\OBS-Studio\bin\64bit\obs64.exe"
;
;
;#KeyHistory 0
;
<!~s::{
	brave_id := WinWait("ahk_exe brave.exe")
	if WinActive(brave_id){
		WinActivate
		Send "^t"
		SendText "brave://sync-internals"
		send "{Enter}"
	}
	return
}

#HotIf GetKeyState("ScrollLock", "T")
; WIN + D
	PrintScreen::Send "#d"
; OPEN TASKMANAGER
	Pause::^+Esc ;Run Taskmgr.exe
; Cycle through items in the order in which they were opened.
	Ins::Send "!{Esc}"
; ALT+TAB
	Home::Send "!{Tab}"
; Win + Tab
	PgUp::Send "#{Tab}"
;
	;Del::
;
	;End::
;
	;PgDn::
;
	UP::!UP
;
	Left::!Left
;
	Down::!Down
;
	Right::!Right
; MESSAGEBOX 
	NumpadHome::MsgBox("AHK is working?",,)
;
	;NumpadUp
; Create New Folder
	NumpadDiv::{
		if (not GetKeyState("Numlock","T")){
			Send "+^{n}" ;Create New Folder
		}
		return
	}
; ScreenShot
	NumpadMult::{
		if( not GetKeyState("Numlock","T")){
			Send "#{PrintScreen}" ;ScreenShot
		}
		return
	}
; CLose Window/App
	NumpadSub::{
		if( not GetKeyState("Numlock","T")){
			Send "!{F4}" ;WinClose A
		}
		return
	}
;
	;NumpadPgUp
/* ;<hoykey fuction>
	NumpadAdd::{
	MsgBox, 4097,<msgbox title>?
		; Type function here

		}
*/
;
	;NumpadLeft
;
	;NumpadClear
;
	;NumpadRight
;
	;NumpadEnd
;
	;NumpadDown 
;
	;NumpadPgDn
;
	;NumpadEnter
;
	;NumpadIns
; Empty Recycle Bin
	NumpadDel::{
		Result := MsgBox("Recycle Bin Warning","Empty the Recycle Bin?","OC")
		If result = "Ok" {
			FileRecycleEmpty
			}
		}
		return 

#HotIf