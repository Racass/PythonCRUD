import alunos
from pyforms.basewidget import BaseWidget
from pyforms.controls   import ControlFile
from pyforms.controls   import ControlText
from pyforms.controls   import ControlSlider
from pyforms.controls   import ControlPlayer
from pyforms.controls   import ControlButton


class ComputerVisionAlgorithm(BaseWidget):
    formMethod = "A"
    alun = alunos.alunos(0)

    def __init__(self, *args, **kwargs):
        super().__init__('Computer vision algorithm example')

        #Definition of the forms fields
        self._ra    = ControlText('RA')
        self._nome = ControlText('nome')
        self._situacao = ControlText('situacao')
        self._syncButton = ControlButton('Ok')

        self._delForm = ControlButton('Modo deletar')
        self._updForm = ControlButton('Modo atualizar')
        self._addForm = ControlButton('Modo adicionar')
        self._getForm = ControlButton('Modo Buscar')

        #Define the event that will be called when the run button is processed
        self._syncButton.value = self.syncEvent
        self._ra.changed_event = self.mudeiRA
        self._nome.changed_event = self.mudeiValor
        self._situacao.changed_event = self.mudeiValor

        self._delForm.value = lambda : self.changeForm('D') #Delete
        self._updForm.value = lambda : self.changeForm('U') #Update
        self._addForm.value = lambda : self.changeForm('A') #Add
        self._getForm.value = lambda : self.changeForm('G') #Get

        self._formset = [
            ('_ra', '_nome', '_situacao'),
            '_syncButton',
            ('_delForm', '_updForm', '_addForm', '_getForm')
        ]
    def mudeiValor(self):
        self.alun.nome = self._nome.value
        self.alun.situacao = bool(self._situacao.value)
        self.changeForm('U')
    def mudeiRA(self):
        self.alun.RA = self._ra.value
    def syncEvent(self):
        if(self.formMethod == "A" or self.formMethod == "U"):
            self.alun.Sync()
        elif(self.formMethod == 'D'):
            self.alun.delete()
        elif(self.formMethod == 'G'):
            self.alun.getAlunos()
            self.updTxts()
            self.changeForm('O')
        pass
    def updTxts(self):
        self._ra.value = str(self.alun.RA)
        self._nome.value = str(self.alun.nome)
        self._situacao.value = str(self.alun.situacao)
    def changeForm(self, method: str):
        self.formMethod = method
        if(method == 'D'): #Delete
            self._syncButton.label = 'Deletar'
            self._ra.enabled = False
        elif(method == 'U'): #Update
            self._syncButton.label = 'Atualizar'
            self._ra.enabled = False
        elif(method == 'A'): #Add
            self.clearToAdd()
            self._syncButton.label = 'Adicionar'
            self._ra.enabled = False
        elif(method == 'G'): #Get
            self.clearScreen()
            self._syncButton.label = 'Buscar'
            self._ra.enabled = True
        elif(method == 'O'): #Ok
            self._syncButton.label = 'Ok'
            self._ra.enabled = False
    def clearToAdd(self):
        self._ra.value = str(self.alun.getNext())
        self._nome.value = ""
        self._situacao.value = ""
    def clearScreen(self):
        self._ra.value = ""
        self._nome.value = ""
        self._situacao.value = ""
if __name__ == '__main__':
    from pyforms import start_app
    start_app(ComputerVisionAlgorithm)
