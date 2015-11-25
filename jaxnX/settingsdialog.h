#ifndef SETTINGSDIALOG_H
#define SETTINGSDIALOG_H

#include <QDialog>

namespace Ui {
class settingsdialog;
}

class settingsdialog : public QDialog
{
    Q_OBJECT

public:
    explicit settingsdialog(QWidget *parent = 0);
    ~settingsdialog();

private slots:
    void on_SaveButton_clicked();

    void on_CloseButton_clicked();

private:
    Ui::settingsdialog *ui;
};

#endif // SETTINGSDIALOG_H
