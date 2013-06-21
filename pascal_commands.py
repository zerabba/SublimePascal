import sublime
import sublime_plugin
import subprocess
import os



class PascalFormat(sublime_plugin.TextCommand):
   def run(self, edit):

            if os.name == "nt":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            self.view.run_command("save")
            process = subprocess.Popen(([os.path.join(sublime.packages_path(), 'SublimePascal', 'format_delphi.bat'), self.view.file_name()]))
            print('Source Formated: ' + self.view.file_name())