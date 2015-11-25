#include "settingsdialog.h"
#include "ui_settingsdialog.h"
#include "dmgmeter.h"
#include <QSettings>

settingsdialog::settingsdialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::settingsdialog)
{
    ui->setupUi(this);
    this->setWindowFlags(Qt::WindowStaysOnTopHint |Qt::FramelessWindowHint);
    QString name;
    name = GW2::DmgMeter::NickName;
    if (name == NULL or name == "" or name.remove(" ").length()==0)
    {
       ui->label_info->setText("Please enter your nickname");
       ui->lineEdit->setFocus();
    }
    else
    {
        ui->lineEdit->setText(name);
    }

}

settingsdialog::~settingsdialog()
{
    delete ui;
}

void settingsdialog::on_SaveButton_clicked()
{
    QString name =  ui->lineEdit->text();
    if (name == NULL or name == "" )
    {
       ui->label_info->setText("Please enter your nickname");
       ui->lineEdit->setFocus();
    }
    else
    {
       QSettings settings("cfg.ini", QSettings::IniFormat);
       settings.beginGroup("General");
       settings.setValue("Name",name);
       settings.endGroup();
       settings.sync();
       GW2::DmgMeter::NickName=name;
       ui->label_info->clear();
    }

}

void settingsdialog::on_CloseButton_clicked()
{
    this->close();
}
