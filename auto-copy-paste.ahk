#Persistent
OnClipboardChange("PasteClipboard")
Return

PasteClipboard()
{
	SendInput %Clipboard%{Enter}
}
