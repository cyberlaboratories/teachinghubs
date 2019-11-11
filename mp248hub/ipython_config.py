c = get_config()

#set matplotlib backend to inline
#c.InteractiveShellApp.matplotlib = None
#c.InteractiveShellApp.gui = None
#c.InteractiveShellApp.pylab = "inline"
c.InteractiveShellApp.exec_lines = [
    "%pylab inline\n"
]
# "display(HTML(\'<style>.container { width:80% !important; }</style>\'))
#"%nbagg\n",
#]

#c.NotebookNotary.data_dir="/home/user/.secret"
#c.NotebookNotary.db_file= "/home/user/.secret/nbsignatures.db"
#c.NotebookNotary.db_file= "/home/user/.secret/nbsignatures.db"
#c.NotebookApp.secret_file="/home/user/.secret/notebook_secret"

#c.NotebookApp.secret_file="/home/user/.local/share/jupyter/notebook_secret"
#c.update({"load_extensions":{"init_cell/main":True}})
