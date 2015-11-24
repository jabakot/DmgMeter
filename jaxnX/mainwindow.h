#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#define MAINWINDOW_WEBSITE_URL "http://www.gw2dmg-meter.de/howto.html"

#include <QMainWindow>
#include "screenrecorderthread.h"
#include <QMouseEvent>

namespace Ui {
    class MainWindow;
}

namespace GW2
{
    class MainWindow : public QMainWindow
    {
        Q_OBJECT

    private:
        Ui::MainWindow *ui;
        ScreenRecorderThread m_RecorderThread;
        void mousePressEvent(QMouseEvent *event);
        void mouseMoveEvent(QMouseEvent *event);
        int m_nMouseClick_X_Coordinate;
        int m_nMouseClick_Y_Coordinate;

    public:
        explicit MainWindow(QWidget *parent = 0);
        ~MainWindow();

    private slots:
        void EnableOpacity(bool isOpaque);
        void LinkToWebsite();
        void on_actionExit_triggered();
    };
}


#endif // MAINWINDOW_H
