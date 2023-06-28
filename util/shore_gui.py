from nicegui import ui, events
from deploy import Deployer
import os


with ui.dialog().props('full-width') as dialog:
    with ui.card():
        content = ui.markdown()

log = ui.log(max_lines=200).classes('w-full h-full')

spinner = ui.spinner(size='lg')
spinner.set_visibility(False)
def clicked():
    spinner.set_visibility(True)
    ui.update()
    log.push(Deployer.send())
    log.push(Deployer.build())
    spinner.set_visibility(False)

    # content.set_content(output.decode("utf-8"))
    # dialog.open()


ui.button('Deploy', on_click=clicked)

ui.run()


ui.run(title="Submit File")