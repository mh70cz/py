
Preferences: Open keyboard shortcuts JSON

    {
        // set current working directory 
		// https://stackoverflow.com/questions/56218958/how-to-quickly-change-shell-folder-to-match-the-currently-open-file
        "key": "ctrl+alt+d",
        "command": "workbench.action.terminal.sendSequence",
        "args": {"text": "cd /d \"${fileDirname}\"\u000D"}
    }

...




