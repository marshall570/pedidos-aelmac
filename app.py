# -*- coding: utf-8 -*-
import tkinter
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from dto import Pedidos
from dao import Dao
from tkinter import messagebox

p = Pedidos()
dao = Dao()


class Ui_FormPedidos(object):
    ############################################################
    # Form variables
    ############################################################    
    message = ''


    ############################################################
    # Passive methods
    ############################################################    
    def disable_readOnly(self):
        self.txtAssistido.setReadOnly(False)
        self.cmbNecessidade.setEnabled(True)
        self.txtIdade.setReadOnly(False)
        self.txtInicio.setReadOnly(False)
        self.txtFim.setReadOnly(False)
        self.txtSolicitante.setReadOnly(False)
        self.txtEmail.setReadOnly(False)
        self.txtTelefone.setReadOnly(False)
        self.txtEndereco.setReadOnly(False)
        self.txtObs.setReadOnly(False)
        self.checkAcidentes.setEnabled(True)
        self.checkPsiquiatrico.setEnabled(True)
        self.checkDependencia.setEnabled(True)
        self.checkDesemprego.setEnabled(True)
        self.checkHospital.setEnabled(True)
        self.checkCirurgia.setEnabled(True)
        self.checkFalecimento.setEnabled(True)
        self.checkPreso.setEnabled(True)
        self.checkObsessivo.setEnabled(True)
        self.checkDesaparecimento.setEnabled(True)
        self.checkSequestro.setEnabled(True)
        self.checkSuicidio.setEnabled(True)
        self.checkDepressao.setEnabled(True)
        self.checkOutro.setEnabled(True)

    def enable_readOnly(self):
        self.txtAssistido.setReadOnly(True)
        self.cmbNecessidade.setEnabled(False)
        self.txtIdade.setReadOnly(True)
        self.txtInicio.setReadOnly(True)
        self.txtFim.setReadOnly(True)
        self.txtSolicitante.setReadOnly(True)
        self.txtEmail.setReadOnly(True)
        self.txtTelefone.setReadOnly(True)
        self.txtEndereco.setReadOnly(True)
        self.txtObs.setReadOnly(True)
        self.checkAcidentes.setEnabled(False)
        self.checkPsiquiatrico.setEnabled(False)
        self.checkDependencia.setEnabled(False)
        self.checkDesemprego.setEnabled(False)
        self.checkHospital.setEnabled(False)
        self.checkCirurgia.setEnabled(False)
        self.checkFalecimento.setEnabled(False)
        self.checkPreso.setEnabled(False)
        self.checkObsessivo.setEnabled(False)
        self.checkDesaparecimento.setEnabled(False)
        self.checkSequestro.setEnabled(False)
        self.checkSuicidio.setEnabled(False)
        self.checkDepressao.setEnabled(False)
        self.checkOutro.setEnabled(False)
        self.txtOutro.setReadOnly(True)

    def enable_navigation(self):
        self.txtIndex.setEnabled(True)

    def disable_navigation(self):
        self.txtIndex.setEnabled(False)

    def enable_export(self):
        self.btnExportAll.setEnabled(True)
        self.btnExportOne.setEnabled(True)

    def disable_export(self):
        self.btnExportAll.setEnabled(False)
        self.btnExportOne.setEnabled(False)

    def clear_form(self):
        self.txtAssistido.setText('')

        self.txtIdade.setText('')
        self.txtInicio.setText('')
        self.txtFim.setText('')
        self.txtSolicitante.setText('')
        self.txtEmail.setText('')
        self.txtTelefone.setText('')
        self.txtEndereco.setText('')
        self.txtObs.setText('')

        if self.checkAcidentes.isChecked():
            self.checkAcidentes.toggle()

        if self.checkPsiquiatrico.isChecked():
            self.checkPsiquiatrico.toggle()

        if self.checkDependencia.isChecked():
            self.checkDependencia.toggle()

        if self.checkDesemprego.isChecked():
            self.checkDesemprego.toggle()

        if self.checkHospital.isChecked():
            self.checkHospital.toggle()

        if self.checkCirurgia.isChecked():
            self.checkCirurgia.toggle()

        if self.checkFalecimento.isChecked():
            self.checkFalecimento.toggle()

        if self.checkPreso.isChecked():
            self.checkPreso.toggle()

        if self.checkObsessivo.isChecked():
            self.checkObsessivo.toggle()

        if self.checkDesaparecimento.isChecked():
            self.checkDesaparecimento.toggle()

        if self.checkSequestro.isChecked():
            self.checkSequestro.toggle()

        if self.checkSuicidio.isChecked():
            self.checkSuicidio.toggle()

        if self.checkDepressao.isChecked():
            self.checkDepressao.toggle()

        if self.checkOutro.isChecked():
            self.checkOutro.toggle()

        self.txtOutro.setReadOnly(True)
        self.txtOutro.setText('')

    def fill_form(self):
        self.clear_form()
        # results = []
        results = dao.select(self.txtIndex.value())
        
        p.code = results[0]
        p.register_date = results[1]
        p.assisted = results[2]
        p.need = results[3]
        p.age = results[4]
        p.beginning = results[5]
        p.ending = results[6]
        p.requester = results[7]
        p.email = results[8]
        p.phone = results[9]
        p.address = results[10]
        p.observations = results[11]
        p.info = results[12]        
        
        
        self.txtAssistido.setText(p.assisted)

        self.cmbNecessidade.setCurrentText(p.need)

        self.txtIdade.setText(p.age)
        self.txtInicio.setText(p.beginning)
        self.txtFim.setText(p.ending)
        self.txtSolicitante.setText(p.requester)
        self.txtEmail.setText(p.email)
        self.txtTelefone.setText(p.phone)
        self.txtEndereco.setText(p.address)
        self.txtObs.setText(p.observations)

        if p.info.find('Acidentes') != -1:
            self.checkAcidentes.toggle()

        if p.info.find('Caso psiquiátrico') != -1:
            self.checkPsiquiatrico.toggle()

        if p.info.find('Dependências') != -1:
            self.checkDependencia.toggle()

        if p.info.find('Desemprego') != -1:
            self.checkDesemprego.toggle()

        if p.info.find('Hospitalização') != -1:
            self.checkHospital.toggle()

        if p.info.find('Cirurgia') != -1:
            self.checkCirurgia.toggle()

        if p.info.find('Falecimento') != -1:
            self.checkFalecimento.toggle()

        if p.info.find('Preso') != -1:
            self.checkPreso.toggle()

        if p.info.find('Problema obsessivo') != -1:
            self.checkObsessivo.toggle()

        if p.info.find('Desaparecimento') != -1:
            self.checkDesaparecimento.toggle()

        if p.info.find('Sequestro') != -1:
            self.checkSequestro.toggle()

        if p.info.find('Tentativa de suicídio') != -1:
            self.checkSuicidio.toggle()

        if p.info.find('Depressão') != -1:
            self.checkDepressao.toggle()

        if p.info.find(' --- ') != -1:
            self.checkOutro.toggle()
            self.txtOutro.setText(p.info.split(' --- ')[1])
        else:
            self.txtOutro.setText('')
        self.txtOutro.setReadOnly(True)

    def check_fields(self):
        self.message = ''
        
        if len(self.txtAssistido.text().strip()) < 3:
            self.message += '- Nome do assistido inválido\n'
            
        if not self.txtIdade.text().isdigit() and len(self.txtIdade.text().strip()) < 1:
            self.message += '- Idade inválida\n'            
            
        if len(self.txtFim.text()) < len(self.txtInicio.text()) or not self.check_date(self.txtFim.text().strip()) or self.txtFim.text() == self.txtInicio.text():
            self.message += '- Data de Término inválida\n'
            
        if len(self.txtSolicitante.text().strip()) < 3:
            self.message += '- Nome do Solicitante inválido'
            
        if len(self.message) >= 1:
            return True
        else:
            return False
 
    def check_date(self, data):
            import datetime
            
            today = datetime.datetime.now()        
            
            date = data.split('/')
            day = int(date[0])
            month = int(date[1])
            year = int(date[2])
            
            if year < today.year:
                return False
            else:
                if month > 12 or month < 1:
                    return False
                else:
                    if day < 1:
                        return False
                    else:
                        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                            if day > 31:
                                return False
                        elif month == 2:
                            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                                if day > 29:
                                    return False
                            else:
                                if day > 28:
                                    return False
                        else:
                            if day > 30:
                                return False
            return True
                    
    def treat_fields(self):
        if self.check_fields():
            root = tkinter.Tk()
            root.withdraw()
            
            messagebox.showerror('ERRO', 'ERRO, Não é possível concluir o cadastro devido os seguintes erros:\n\n' + self.message)            
            tkinter.Tk().destroy()
            self.txtAssistido.setFocus()
        else:
            root = tkinter.Tk()
            root.withdraw()
            
            choice = messagebox.askyesno('CONFIRMAR REGISTRO', 'Deseja cadastrar esse pedido?')
            tkinter.Tk().destroy()
            if choice == True:    
                today = datetime.datetime.now().strftime('%d/%m/%Y')

                p.code = dao.id_gen()
                p.register_date = today
                p.assisted = self.txtAssistido.text().strip().title()
                p.need = self.cmbNecessidade.currentText()

                p.age = self.txtIdade.text().strip()
                p.beginning = self.txtInicio.text().strip()
                p.ending = self.txtFim.text().strip()
                p.requester = self.txtSolicitante.text().strip().title()
                p.email = self.txtEmail.text().strip()
                p.phone = self.txtTelefone.text().strip()
                p.address = self.txtEndereco.text().strip().title()
                p.observations = self.txtObs.toPlainText().strip()
                                
                infos = ''                
                
                if self.checkAcidentes.isChecked():
                    infos += 'Acidentes, '
                if self.checkPsiquiatrico.isChecked():
                    infos += 'Caso psiquiátrico, '
                if self.checkDependencia.isChecked():
                    infos += 'Dependências, '
                if self.checkDesemprego.isChecked():
                    infos += 'Desemprego, '
                if self.checkHospital.isChecked():
                    infos += 'Hospitalização, '
                if self.checkCirurgia.isChecked():
                    infos += 'Cirurgia, '
                if self.checkFalecimento.isChecked():
                    infos += 'Falecimento, '
                if self.checkPreso.isChecked():
                    infos += 'Preso, '
                if self.checkObsessivo.isChecked():
                    infos += 'Problema obsessivo, '
                if self.checkDesaparecimento.isChecked():
                    infos += 'Desaparecimento, '
                if self.checkSequestro.isChecked():
                    infos += 'Sequestro, '
                if self.checkSuicidio.isChecked():
                    infos += 'Tentativa de suicídio, '
                if self.checkDepressao.isChecked():
                    infos += 'Depressão'
                
                if infos.endswith(', '):
                    infos = infos[:-2]
                
                if len(self.txtOutro.toPlainText()) > 2:
                    infos += ' --- ' + self.txtOutro.toPlainText()
                
                p.info = infos
                
                dao.insert(p)
                self.txtIndex.setMaximum(dao.id_gen() - 1)
                self.btn_add_clicked()
                self.enable_export()

    def navigation_buttons(self):
        total = dao.id_gen() - 1

        if total <= 1:
            self.disable_navigation()
            self.disable_export()


    ############################################################
    # buttons methods
    ############################################################    
    def btn_add_clicked(self):
        today = datetime.datetime.now().strftime('%d/%m/%Y')
        
        if self.txtAssistido.isReadOnly():
            self.disable_readOnly()
            self.disable_navigation()
            self.disable_export()
            self.clear_form()

            self.btnSave.setEnabled(True)
            new_icon = QtGui.QIcon.fromTheme('dialog-cancel')
            self.btnAdd.setIcon(new_icon)
            self.btnAdd.setIconSize(QtCore.QSize(24, 24))
            self.btnAdd.setText('CANCELAR')
            self.btnSave.setEnabled(True)
            self.txtAssistido.setFocus(True)
            self.txtInicio.setText(today)
            self.txtInicio.setReadOnly(True)
        else:
            self.enable_readOnly()
            self.enable_navigation()
            self.enable_export()
            self.fill_form()

            self.btnSave.setEnabled(True)
            new_icon = QtGui.QIcon.fromTheme('list-add')
            self.btnAdd.setIcon(new_icon)
            self.btnAdd.setIconSize(QtCore.QSize(24, 24))
            self.btnAdd.setText('ADICIONAR')
            self.btnSave.setEnabled(False)

    def check_outro_clicked(self):
        if self.checkOutro.isChecked():
            self.txtOutro.setEnabled(True)
            self.txtOutro.setReadOnly(False)
        else:
            self.txtOutro.setReadOnly(True)
            self.txtOutro.setText('')

    def btn_save_clicked(self):
        self.treat_fields()

    def txt_index_changed(self):        
        if self.txtIndex.value() != 0:
            self.fill_form()

    def btn_export_all_clicked(self):
        root = tkinter.Tk()
        root.withdraw()
        choice = messagebox.askyesno('EXPORTAR PARA EXCEL', 'Deseja criar relatório com os pedidos a partir do pedido Nº' + str(p.code) + '?')
        tkinter.Tk().destroy()
        
        if choice == True:    
            dao.gen_excel(p)
    
    def btn_export_one_clicked(self):
        root = tkinter.Tk()
        root.withdraw()
        choice = messagebox.askyesno('IMPRIMIR PEDIDO', 'Deseja criar um arquivo para impressão deste pedido?')
        tkinter.Tk().destroy()
        
        if choice == True:
            dao.gen_pdf(p)
     
     
        
    ############################################################
    # QT Designer methods
    ############################################################    
    def setupUi(self, FormPedidos):
        FormPedidos.setObjectName('FormPedidos')
        FormPedidos.resize(763, 656)
        FormPedidos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        FormPedidos.setWindowTitle('PEDIDOS DE ORACAO')
        self.centralwidget = QtWidgets.QWidget(FormPedidos)
        self.centralwidget.setObjectName('centralwidget')
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName('gridLayout')
        self.txtObs = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtObs.setFont(font)
        self.txtObs.setObjectName('txtObs')
        self.gridLayout.addWidget(self.txtObs, 13, 0, 3, 4)
        self.txtTelefone = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        self.txtTelefone.setFont(font)
        self.txtTelefone.setInputMask('(##) #########')
        self.txtTelefone.setText('')
        self.txtTelefone.setObjectName('txtTelefone')
        self.gridLayout.addWidget(self.txtTelefone, 9, 3, 1, 1)
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.btnAdd.setFont(font)
        self.btnAdd.setText('ADICIONAR')
        icon = QtGui.QIcon.fromTheme('list-add')
        self.btnAdd.setIcon(icon)
        self.btnAdd.setIconSize(QtCore.QSize(24, 24))
        self.btnAdd.setObjectName('btnAdd')
        self.gridLayout.addWidget(self.btnAdd, 14, 4, 1, 1)
        self.lblTelefone = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblTelefone.setFont(font)
        self.lblTelefone.setText('TELEFONE')
        self.lblTelefone.setObjectName('lblTelefone')
        self.gridLayout.addWidget(self.lblTelefone, 8, 3, 1, 1)
        self.btnExportAll = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.btnExportAll.setFont(font)
        self.btnExportAll.setText('EXPORTAR REGISTROS')
        icon = QtGui.QIcon.fromTheme('x-office-spreadsheet')
        self.btnExportAll.setIcon(icon)
        self.btnExportAll.setIconSize(QtCore.QSize(24, 24))
        self.btnExportAll.setObjectName('btnExportAll')
        self.gridLayout.addWidget(self.btnExportAll, 16, 4, 1, 2)
        self.lblObs = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblObs.setFont(font)
        self.lblObs.setText('OBSERVAÇÕES')
        self.lblObs.setObjectName('lblObs')
        self.gridLayout.addWidget(self.lblObs, 12, 0, 1, 1)
        self.txtInicio = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        self.txtInicio.setFont(font)
        self.txtInicio.setInputMask('##/##/####')
        self.txtInicio.setText('')
        self.txtInicio.setAlignment(QtCore.Qt.AlignCenter)
        self.txtInicio.setObjectName('txtInicio')
        self.gridLayout.addWidget(self.txtInicio, 5, 2, 1, 1)
        self.lblAssistido = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblAssistido.setFont(font)
        self.lblAssistido.setText('NOME DO ASSISTIDO')
        self.lblAssistido.setObjectName('lblAssistido')
        self.gridLayout.addWidget(self.lblAssistido, 0, 0, 1, 3)
        self.txtIndex = QtWidgets.QSpinBox(self.centralwidget)
        self.txtIndex.setObjectName('txtIndex')
        self.gridLayout.addWidget(self.txtIndex, 16, 0, 1, 4)
        self.gpInfo = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.gpInfo.setFont(font)
        self.gpInfo.setTitle('INFO PARA O DEPOE')
        self.gpInfo.setObjectName('gpInfo')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gpInfo)
        self.verticalLayout.setObjectName('verticalLayout')
        self.checkAcidentes = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkAcidentes.setFont(font)
        self.checkAcidentes.setText('Acidentes')
        self.checkAcidentes.setObjectName('checkAcidentes')
        self.verticalLayout.addWidget(self.checkAcidentes)
        self.checkPsiquiatrico = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkPsiquiatrico.setFont(font)
        self.checkPsiquiatrico.setText('Caso psiquiátrico')
        self.checkPsiquiatrico.setObjectName('checkPsiquiatrico')
        self.verticalLayout.addWidget(self.checkPsiquiatrico)
        self.checkDependencia = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkDependencia.setFont(font)
        self.checkDependencia.setText('Dependências')
        self.checkDependencia.setObjectName('checkDependencia')
        self.verticalLayout.addWidget(self.checkDependencia)
        self.checkDesemprego = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkDesemprego.setFont(font)
        self.checkDesemprego.setText('Desemprego')
        self.checkDesemprego.setObjectName('checkDesemprego')
        self.verticalLayout.addWidget(self.checkDesemprego)
        self.checkHospital = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkHospital.setFont(font)
        self.checkHospital.setText('Hospitalização')
        self.checkHospital.setObjectName('checkHospital')
        self.verticalLayout.addWidget(self.checkHospital)
        self.checkCirurgia = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkCirurgia.setFont(font)
        self.checkCirurgia.setText('Cirurgia')
        self.checkCirurgia.setObjectName('checkCirurgia')
        self.verticalLayout.addWidget(self.checkCirurgia)
        self.checkFalecimento = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkFalecimento.setFont(font)
        self.checkFalecimento.setText('Falecimento')
        self.checkFalecimento.setObjectName('checkFalecimento')
        self.verticalLayout.addWidget(self.checkFalecimento)
        self.checkPreso = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkPreso.setFont(font)
        self.checkPreso.setText('Preso')
        self.checkPreso.setObjectName('checkPreso')
        self.verticalLayout.addWidget(self.checkPreso)
        self.checkObsessivo = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkObsessivo.setFont(font)
        self.checkObsessivo.setText('Prob. Obsessivo')
        self.checkObsessivo.setObjectName('checkObsessivo')
        self.verticalLayout.addWidget(self.checkObsessivo)
        self.checkDesaparecimento = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkDesaparecimento.setFont(font)
        self.checkDesaparecimento.setText('Desaparecimento')
        self.checkDesaparecimento.setObjectName('checkDesaparecimento')
        self.verticalLayout.addWidget(self.checkDesaparecimento)
        self.checkSequestro = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkSequestro.setFont(font)
        self.checkSequestro.setText('Sequestro')
        self.checkSequestro.setObjectName('checkSequestro')
        self.verticalLayout.addWidget(self.checkSequestro)
        self.checkSuicidio = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkSuicidio.setFont(font)
        self.checkSuicidio.setText('Tentativa de Suicídio')
        self.checkSuicidio.setObjectName('checkSuicidio')
        self.verticalLayout.addWidget(self.checkSuicidio)
        self.checkDepressao = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkDepressao.setFont(font)
        self.checkDepressao.setText('Depressão')
        self.checkDepressao.setObjectName('checkDepressao')
        self.verticalLayout.addWidget(self.checkDepressao)
        self.checkOutro = QtWidgets.QCheckBox(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkOutro.setFont(font)
        self.checkOutro.setText('Outro:')
        self.checkOutro.setObjectName('checkOutro')
        self.verticalLayout.addWidget(self.checkOutro)
        self.txtOutro = QtWidgets.QTextEdit(self.gpInfo)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.txtOutro.setFont(font)
        self.txtOutro.setObjectName('txtOutro')
        self.verticalLayout.addWidget(self.txtOutro)
        self.gridLayout.addWidget(self.gpInfo, 0, 4, 14, 2)
        self.txtEndereco = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        self.txtEndereco.setFont(font)
        self.txtEndereco.setText('')
        self.txtEndereco.setObjectName('txtEndereco')
        self.gridLayout.addWidget(self.txtEndereco, 11, 0, 1, 4)
        self.lblEndereco = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblEndereco.setFont(font)
        self.lblEndereco.setText('ENDEREÇO')
        self.lblEndereco.setObjectName('lblEndereco')
        self.gridLayout.addWidget(self.lblEndereco, 10, 0, 1, 1)
        self.txtEmail = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        self.txtEmail.setFont(font)
        self.txtEmail.setText('')
        self.txtEmail.setObjectName('txtEmail')
        self.gridLayout.addWidget(self.txtEmail, 9, 0, 1, 3)
        self.lblInicio = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblInicio.setFont(font)
        self.lblInicio.setText('DATA DE INÍCIO')
        self.lblInicio.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInicio.setObjectName('lblInicio')
        self.gridLayout.addWidget(self.lblInicio, 4, 2, 1, 1)
        self.lblSolicitante = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblSolicitante.setFont(font)
        self.lblSolicitante.setText('NOME DO SOLICITANTE')
        self.lblSolicitante.setObjectName('lblSolicitante')
        self.gridLayout.addWidget(self.lblSolicitante, 6, 0, 1, 3)
        self.txtSolicitante = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        self.txtSolicitante.setFont(font)
        self.txtSolicitante.setText('')
        self.txtSolicitante.setObjectName('txtSolicitante')
        self.gridLayout.addWidget(self.txtSolicitante, 7, 0, 1, 4)
        self.txtFim = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        self.txtFim.setFont(font)
        self.txtFim.setInputMask('##/##/####')
        self.txtFim.setText('')
        self.txtFim.setAlignment(QtCore.Qt.AlignCenter)
        self.txtFim.setObjectName('txtFim')
        self.gridLayout.addWidget(self.txtFim, 5, 3, 1, 1)
        self.lblIdade = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblIdade.setFont(font)
        self.lblIdade.setText('IDADE')
        self.lblIdade.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIdade.setObjectName('lblIdade')
        self.gridLayout.addWidget(self.lblIdade, 4, 0, 1, 2)
        self.lblEmail = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblEmail.setFont(font)
        self.lblEmail.setText('E-MAIL')
        self.lblEmail.setObjectName('lblEmail')
        self.gridLayout.addWidget(self.lblEmail, 8, 0, 1, 1)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.btnSave.setFont(font)
        self.btnSave.setText('SALVAR')
        icon = QtGui.QIcon.fromTheme('document-save')
        self.btnSave.setIcon(icon)
        self.btnSave.setIconSize(QtCore.QSize(24, 24))
        self.btnSave.setObjectName('btnSave')
        self.gridLayout.addWidget(self.btnSave, 14, 5, 1, 1)
        self.btnExportOne = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.btnExportOne.setFont(font)
        self.btnExportOne.setText('IMPRIMIR REGISTRO ATUAL')
        icon = QtGui.QIcon.fromTheme('document-print')
        self.btnExportOne.setIcon(icon)
        self.btnExportOne.setIconSize(QtCore.QSize(24, 24))
        self.btnExportOne.setObjectName('btnExportOne')
        self.gridLayout.addWidget(self.btnExportOne, 15, 4, 1, 2)
        self.txtIdade = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        self.txtIdade.setFont(font)
        self.txtIdade.setInputMask('###')
        self.txtIdade.setText('')
        self.txtIdade.setAlignment(QtCore.Qt.AlignCenter)
        self.txtIdade.setObjectName('txtIdade')
        self.gridLayout.addWidget(self.txtIdade, 5, 0, 1, 2)
        self.lblFim = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblFim.setFont(font)
        self.lblFim.setText('DATA DE TÉRMINO')
        self.lblFim.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFim.setObjectName('lblFim')
        self.gridLayout.addWidget(self.lblFim, 4, 3, 1, 1)
        self.txtAssistido = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(10)
        self.txtAssistido.setFont(font)
        self.txtAssistido.setText('')
        self.txtAssistido.setObjectName('txtAssistido')
        self.gridLayout.addWidget(self.txtAssistido, 1, 0, 1, 4)
        self.lblIdade_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Ubuntu')
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblIdade_2.setFont(font)
        self.lblIdade_2.setText('NECESSIDADE')
        self.lblIdade_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIdade_2.setObjectName('lblIdade_2')
        self.gridLayout.addWidget(self.lblIdade_2, 2, 0, 1, 1)
        self.cmbNecessidade = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cmbNecessidade.setFont(font)
        self.cmbNecessidade.setCurrentText('Físico')
        self.cmbNecessidade.setObjectName('cmbNecessidade')
        self.cmbNecessidade.addItem('')
        self.cmbNecessidade.setItemText(0, 'Físico')
        self.cmbNecessidade.addItem('')
        self.cmbNecessidade.setItemText(1, 'Desencarnada')
        self.cmbNecessidade.addItem('')
        self.cmbNecessidade.setItemText(2, 'Espiritual')
        self.gridLayout.addWidget(self.cmbNecessidade, 3, 0, 1, 4)
        FormPedidos.setCentralWidget(self.centralwidget)
           
        self.btnAdd.clicked.connect(self.btn_add_clicked)
        self.btnExportAll.clicked.connect(self.btn_export_all_clicked)
        self.btnExportOne.clicked.connect(self.btn_export_one_clicked)
        self.txtIndex.valueChanged.connect(self.txt_index_changed)
        self.btnSave.clicked.connect(self.btn_save_clicked)
        self.checkOutro.clicked.connect(self.check_outro_clicked)                
        
        self.enable_readOnly()

        if dao.id_gen() - 1 < 1:
            self.clear_form()
            self.txtIndex.setMinimum(0)                     
            self.txtIndex.setMaximum(0)
            self.txtIndex.setValue(0)
            self.navigation_buttons()
        else:            
            self.txtIndex.setMinimum(1)                     
            self.txtIndex.setMaximum(dao.id_gen() - 1)
            self.txtIndex.setValue(dao.id_gen() - 1)
            self.navigation_buttons()
            self.enable_export()        

        QtCore.QMetaObject.connectSlotsByName(FormPedidos)
        FormPedidos.setTabOrder(self.txtAssistido, self.cmbNecessidade)
        FormPedidos.setTabOrder(self.cmbNecessidade, self.txtIdade)
        FormPedidos.setTabOrder(self.txtIdade, self.txtInicio)
        FormPedidos.setTabOrder(self.txtInicio, self.txtFim)
        FormPedidos.setTabOrder(self.txtFim, self.txtSolicitante)
        FormPedidos.setTabOrder(self.txtSolicitante, self.txtEmail)
        FormPedidos.setTabOrder(self.txtEmail, self.txtTelefone)
        FormPedidos.setTabOrder(self.txtTelefone, self.txtEndereco)
        FormPedidos.setTabOrder(self.txtEndereco, self.txtObs)
        FormPedidos.setTabOrder(self.txtObs, self.checkAcidentes)
        FormPedidos.setTabOrder(self.checkAcidentes, self.checkPsiquiatrico)
        FormPedidos.setTabOrder(self.checkPsiquiatrico, self.checkDependencia)
        FormPedidos.setTabOrder(self.checkDependencia, self.checkDesemprego)
        FormPedidos.setTabOrder(self.checkDesemprego, self.checkHospital)
        FormPedidos.setTabOrder(self.checkHospital, self.checkCirurgia)
        FormPedidos.setTabOrder(self.checkCirurgia, self.checkFalecimento)
        FormPedidos.setTabOrder(self.checkFalecimento, self.checkPreso)
        FormPedidos.setTabOrder(self.checkPreso, self.checkObsessivo)
        FormPedidos.setTabOrder(self.checkObsessivo, self.checkDesaparecimento)
        FormPedidos.setTabOrder(self.checkDesaparecimento, self.checkSequestro)
        FormPedidos.setTabOrder(self.checkSequestro, self.checkSuicidio)
        FormPedidos.setTabOrder(self.checkSuicidio, self.checkDepressao)
        FormPedidos.setTabOrder(self.checkDepressao, self.checkOutro)
        FormPedidos.setTabOrder(self.checkOutro, self.txtOutro)
        FormPedidos.setTabOrder(self.txtOutro, self.btnAdd)
        FormPedidos.setTabOrder(self.btnAdd, self.btnSave)
        FormPedidos.setTabOrder(self.btnSave, self.btnExportOne)
        FormPedidos.setTabOrder(self.btnExportOne, self.btnExportAll)
        FormPedidos.setTabOrder(self.btnExportAll, self.txtIndex)


if __name__ == '__main__':
    import sys
    dao.create_table()    
    dao.create_directories()
    app = QtWidgets.QApplication(sys.argv)
    FormPedidos = QtWidgets.QMainWindow()
    ui = Ui_FormPedidos()
    ui.setupUi(FormPedidos)
    FormPedidos.show()
    sys.exit(app.exec_())
