#An application which can be used for Mass RT on twitter(not fully tested)
'''
Enter the Access Key,Access Secret,consumer Key,consumer Secret of all the accounts that are to be a part of the
RT network in LoginTab table in LoginDetails.db. A separate registration page is provided for the same have been
provided in the application for ease.
Once a tweet is sent, it will be retweeted by all the users registered in the database.  
'''

from PyQt4 import QtCore, QtGui
import tweepy
import sys
from TwitterAPI import TwitterAPI
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
import os
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
import sqlite3
class Ui_Form(object):
    LoginDB = sqlite3.connect('LoginDetails.db')
    databaseCursor = LoginDB.cursor()
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(473, 345)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 30, 391, 301))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.label_5 = QtGui.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(110, 200, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.UsernameRegTxt = QtGui.QTextEdit(self.page_3)
        self.UsernameRegTxt.setGeometry(QtCore.QRect(210, 30, 104, 31))
        self.UsernameRegTxt.setObjectName(_fromUtf8("UsernameRegTxt"))
        self.ConsumerSecretTxt = QtGui.QTextEdit(self.page_3)
        self.ConsumerSecretTxt.setGeometry(QtCore.QRect(210, 190, 104, 31))
        self.ConsumerSecretTxt.setObjectName(_fromUtf8("ConsumerSecretTxt"))
        self.label_3 = QtGui.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(110, 40, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.AccessSecretTxt = QtGui.QTextEdit(self.page_3)
        self.AccessSecretTxt.setGeometry(QtCore.QRect(210, 110, 104, 31))
        self.AccessSecretTxt.setObjectName(_fromUtf8("AccessSecretTxt"))
        self.label_4 = QtGui.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(110, 120, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.RegisterBtn_2 = QtGui.QPushButton(self.page_3)
        self.RegisterBtn_2.setGeometry(QtCore.QRect(170, 250, 75, 23))
        self.RegisterBtn_2.setObjectName(_fromUtf8("RegisterBtn_2"))
        self.AccessKeyTxt = QtGui.QTextEdit(self.page_3)
        self.AccessKeyTxt.setGeometry(QtCore.QRect(210, 70, 104, 31))
        self.AccessKeyTxt.setObjectName(_fromUtf8("AccessKeyTxt"))
        self.label_6 = QtGui.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(110, 80, 51, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.ConsumerKeyTxt = QtGui.QTextEdit(self.page_3)
        self.ConsumerKeyTxt.setGeometry(QtCore.QRect(210, 150, 104, 31))
        self.ConsumerKeyTxt.setObjectName(_fromUtf8("ConsumerKeyTxt"))
        self.label_7 = QtGui.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(110, 160, 71, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.stackedWidget.addWidget(self.page_3)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.LoginBtn = QtGui.QPushButton(self.page)
        self.LoginBtn.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.LoginBtn.setObjectName(_fromUtf8("LoginBtn"))
        self.UsernameTxt = QtGui.QPlainTextEdit(self.page)
        self.UsernameTxt.setGeometry(QtCore.QRect(120, 80, 191, 31))
        self.UsernameTxt.setObjectName(_fromUtf8("UsernameTxt"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.RegisterBtn = QtGui.QPushButton(self.page)
        self.RegisterBtn.setGeometry(QtCore.QRect(210, 150, 75, 23))
        self.RegisterBtn.setObjectName(_fromUtf8("RegisterBtn"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.UploadBtn = QtGui.QPushButton(self.page_2)
        self.UploadBtn.setGeometry(QtCore.QRect(260, 180, 75, 23))
        self.UploadBtn.setObjectName(_fromUtf8("UploadBtn"))
        self.label = QtGui.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(20, 60, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.TweetBtn = QtGui.QPushButton(self.page_2)
        self.TweetBtn.setGeometry(QtCore.QRect(170, 180, 75, 23))
        self.TweetBtn.setObjectName(_fromUtf8("TweetBtn"))
        self.TweetTxt = QtGui.QPlainTextEdit(self.page_2)
        self.TweetTxt.setGeometry(QtCore.QRect(130, 60, 221, 81))
        self.TweetTxt.setObjectName(_fromUtf8("TweetTxt"))
        self.LoginBtn.clicked.connect(self.loginBtn)
        self.TweetBtn.clicked.connect(self.tweetHandler)
        self.RegisterBtn.clicked.connect(self.registerHandler)
        self.RegisterBtn_2.clicked.connect(self.registerUser)
        self.stackedWidget.addWidget(self.page_2)
        self.UploadBtn.clicked.connect(self.imageHandler)
        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def registerHandler(self):
        self.stackedWidget.setCurrentIndex(0)
    def registerUser(self):
        query="insert into LoginTab values(?,?,?,?,?)";
        self.username=str(self.UsernameRegTxt.toPlainText())
        accessKey=str(self.AccessKeyTxt.toPlainText())
        accessSecret=str(self.AccessSecretTxt.toPlainText())
        consumerKey=str(self.ConsumerKeyTxt.toPlainText())
        consumerSecret=str(self.ConsumerSecretTxt.toPlainText())
        self.databaseCursor.execute(query,(self.username,accessKey,accessSecret,consumerKey,consumerSecret,))
        self.LoginDB.commit()
        QtGui.QMessageBox.about(self.page,'Info','Registration done')
        self.stackedWidget.setCurrentIndex(1)
    
        
    def loginBtn(self):
        self.username=str(self.UsernameTxt.toPlainText())
        query="select * from LoginTab where username=?"
        self.details=self.databaseCursor.execute(query,(self.username,))
        self.users = self.details.fetchall()
        if self.users:
            self.stackedWidget.setCurrentIndex(2)
        else:
            QtGui.QMessageBox.about(self,'Info','Bad username - try again')
        print len(self.users)
    def tweetHandler(self):
        accessKey=self.users[0][1]
        accessSecret=self.users[0][2]
        consumerKey=self.users[0][3]
        consumerSecret=self.users[0][4]
        tweet=str(self.TweetTxt.toPlainText())
        auth=tweepy.OAuthHandler(consumerKey,consumerSecret)
        auth.set_access_token(accessKey,accessSecret)
        api=tweepy.API(auth)
        if self.fn:
            api.update_with_media(self.fn,status=tweet)
        else:
            api.update_status(status=tweet)
        
        auth=tweepy.OAuthHandler(consumerKey,consumerSecret)
        auth.set_access_token(accessKey,accessSecret)
        api=tweepy.API(auth)
        latestTweets = api.user_timeline(screen_name = self.username, count = 1, include_rts = False)
        for tweet in latestTweets:
            tweet_id=tweet.id
        query="select * from LoginTab where username!=?"
        self.details=self.databaseCursor.execute(query,(username,))
        self.users = self.details.fetchall()
        for i in range(0,len(self.users)):
            curAccessKey=self.users[i][1]
            curAccessSecret=self.users[i][2]
            curConsumerKey=self.users[i][3]
            curConsumerSecret=self.users[i][4]
            curAuth=tweepy.OAuthHandler(curConsumerKey,curConsumerSecret)
            curAuth.set_access_token(curAccessKey,curAccessSecret)
            curApi=tweepy.API(curAuth)
            curApi.retweet(tweet_id)

    def imageHandler(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(self.page_3, 'Open file', 
                '')
        self.fn = os.path.abspath(self.fname)
  
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_5.setText(_translate("Form", "Consumer Secret", None))
        self.label_3.setText(_translate("Form", "username", None))
        self.label_4.setText(_translate("Form", "access secret", None))
        self.RegisterBtn_2.setText(_translate("Form", "Register", None))
        self.label_6.setText(_translate("Form", "access key", None))
        self.label_7.setText(_translate("Form", "consumer key", None))
        self.LoginBtn.setText(_translate("Form", "Login", None))
        self.label_2.setText(_translate("Form", "Username", None))
        self.RegisterBtn.setText(_translate("Form", "Register", None))
        self.UploadBtn.setText(_translate("Form", "Upload", None))
        self.label.setText(_translate("Form", "Tweet", None))
        self.TweetBtn.setText(_translate("Form", "Tweet", None))

def main():
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
