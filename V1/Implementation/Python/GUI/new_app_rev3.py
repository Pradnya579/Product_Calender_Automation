"""
App for login
Created by: Govind Bansal
Version 0.4
Date: 06/09/2021
"""
import hashlib
import sqlite3
import os

import streamlit as st
import streamlit.components.v1 as components
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from xlsx2html import xlsx2html

import FacultyCalendarFunction
import FacultyLoadSheetFunction
import MasterCalendarFunction

gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.txt")

drive = GoogleDrive(gauth)


# Security
def make_hashes(password):
    """Function for password encoding"""
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    """Function for checking hashes"""
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# Database creation for faculty details
faculty_user = sqlite3.connect('data.db')
faculty_cursor = faculty_user.cursor()

# Database creation for admin details
admin_user = sqlite3.connect('data2.db')
admin_cursor = admin_user.cursor()


def create_usertable_faculty():
    """Creating table for storing ID and password for faculty"""
    faculty_cursor.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')


def add_userdata_faculty(username, password):
    """Adding new set of ID and password for faculty"""
    faculty_cursor.execute('INSERT INTO userstable(username, password) VALUES (?,?)', (username, password))
    faculty_user.commit()


def login_user_faculty(username, password):
    """Function to login for faculty"""
    faculty_cursor.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = faculty_cursor.fetchall()
    return data


def view_all_users_faculty():
    """Function to fetch all users from DB for faculty"""
    faculty_cursor.execute('SELECT * FROM userstable')
    data = faculty_cursor.fetchall()
    return data


def create_usertable_admin():
    """Creating table for storing ID and password for admin"""
    admin_cursor.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')


def add_userdata_admin(username, password):
    """Adding new set of ID and password for admin"""
    admin_cursor.execute('INSERT INTO userstable(username, password) VALUES (?,?)', (username, password))
    admin_user.commit()


def login_user_admin(username, password):
    """Function to login for admin"""
    admin_cursor.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = admin_cursor.fetchall()
    return data


def view_all_users_admin():
    """Function to fetch all users from DB for admin"""
    admin_cursor.execute('SELECT * FROM userstable')
    data = admin_cursor.fetchall()
    return data


# main function
def main():
    """GUI LOGIN PAGE"""
    st.set_page_config(page_title="GEA Calendar")
    st.title("L&T Technology Services")
    st.sidebar.title("GEA calendar login")
    st.sidebar.markdown("____")
    # Getting Credentials from user
    st.sidebar.subheader("Login using your credentials")
    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password", type='password')
    ac_type = st.sidebar.selectbox("Account Type", ["Faculty", "Admin"])
    if ac_type == "Admin":
        # If account type is admin, provide special privileges
        if st.sidebar.checkbox("Login"):
            # Checking credentials
            create_usertable_admin()
            hashed_password = make_hashes(password)
            result = login_user_admin(username, check_hashes(password, hashed_password))
            if result:
                # If credentials are correct, display menu
                st.sidebar.success("Logged in as {}".format(username))
                st.subheader("Admin Panel")
                menu = st.selectbox("Menu", ["View calendar", "Update calendar", "Download calendar",
                                             "Add new user", "Help"])
                if menu == "View calendar":
                    # Action to view calendar
                    month_view = st.selectbox("Select Month", ["Select", "January", "February", "March", "April",
                                                               "May", "June", "July", "August",
                                                               "September", "October", "November", "December"])

                    # Master Calendar fetching and displaying
                    mc = drive.ListFile({'q': "title contains 'Master' and trashed=false"}).GetList()
                    mc_file_id = mc[0]['id']
                    mc_file = drive.CreateFile({'id': mc_file_id})
                    mc_file_title = 'UpdatedMasterCalendar.xlsx'
                    mc_file.GetContentFile(mc_file_title,
                                           mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    if month_view != "Select":
                        st.subheader("Master Calendar")
                        out_stream_mc = xlsx2html(filepath=mc_file_title,
                                                  sheet=month_view,
                                                  output=(os.getcwd() + "/" + mc_file_title + ".html"),
                                                  default_cell_border="10")
                        out_stream_mc.seek(0)
                        html_file_mc = open(mc_file_title + ".html", 'r', encoding='utf-8')
                        source_code_mc = html_file_mc.read()
                        components.html(source_code_mc, height=500, width=700, scrolling=True)

                    # Faculty Calendar fetching and displaying
                    fc = drive.ListFile({'q': "title contains 'FacultyCalendar' and trashed=false"}).GetList()
                    fc_file_id = fc[0]['id']
                    fc_file = drive.CreateFile({'id': fc_file_id})
                    fc_file_title = 'UpdatedFacultyCalendar.xlsx'
                    fc_file.GetContentFile(fc_file_title,
                                           mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    if month_view != "Select":
                        st.subheader("Faculty Calendar")
                        out_stream_fc = xlsx2html(filepath=fc_file_title,
                                                  sheet=month_view,
                                                  output=(os.getcwd() + "/" + fc_file_title + ".html"),
                                                  default_cell_border=10)
                        out_stream_fc.seek(0)
                        html_file_fc = open(fc_file_title + ".html", 'r', encoding='utf-8')
                        source_code_fc = html_file_fc.read()
                        components.html(source_code_fc, height=500, width=700, scrolling=True)

                    # Faculty Loadsheet fetching and displaying
                    fl = drive.ListFile({'q': "title contains 'FacultyLoad' and trashed=false"}).GetList()
                    fl_file_id = fl[1]['id']
                    fl_file = drive.CreateFile({'id': fl_file_id})
                    fl_file_title = 'UpdatedFacultyLoadSheet.xlsx'
                    fl_file.GetContentFile(fl_file_title,
                                           mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    if month_view != "Select":
                        st.subheader("Faculty Loadsheet")
                        out_stream_fl = xlsx2html(filepath=fl_file_title,
                                                  sheet=month_view,
                                                  output=(os.getcwd() + "/" + fl_file_title + ".html"),
                                                  default_cell_border=10)
                        out_stream_fl.seek(0)
                        html_file_fl = open(fl_file_title + ".html", 'r', encoding='utf-8')
                        source_code_fl = html_file_fl.read()
                        components.html(source_code_fl, height=500, width=700, scrolling=True)

                elif menu == "Update calendar":
                    # Action to update calendar
                    file = st.file_uploader("Upload input file", type=['.xlsx'])
                    month = st.selectbox("Select Month", ["Select", "January", "February", "March", "April",
                                                          "May", "June", "July", "August",
                                                          "September", "October", "November", "December"])
                    initiative = st.selectbox("Select Initiative", ["GENESIS", "GENESIS PRO",
                                                                    "BUILD / STEP UP", "OPEN TRAININGS",
                                                                    "STEPin", "OTHERS"])
                    if st.button("Update calendar"):
                        MasterCalendarFunction.MasterCalendarFunction(file, initiative, month)
                        FacultyCalendarFunction.FacultyCalendarFunction("Test_vector", file, initiative, month)
                        FacultyLoadSheetFunction.FacultyLoadSheetFunction("Test_vector", file, initiative, month)

                    if file is not None:
                        file_details = {"filename": file.name, "filetype": file.type}
                        print(file_details)

                elif menu == "Download calendar":
                    # Downloading master calendar
                    file_list = drive.ListFile({'q': "title contains 'Master' and trashed=false"}).GetList()
                    file_id = file_list[0]['id']
                    file = drive.CreateFile({'id': file_id})
                    file_title = 'UpdatedMasterCalendar.xlsx'
                    file.GetContentFile(file_title,
                                        mimetype='application/vnd.openxmlformats-officedocument'
                                                 '.spreadsheetml.sheet')
                    # Download Faculty Calendar
                    file_list = drive.ListFile({'q': "title contains 'FacultyCalendar' and trashed=false"}) \
                        .GetList()
                    file_id = file_list[0]['id']
                    file = drive.CreateFile({'id': file_id})
                    file_title = 'UpdatedFacultyCalendar.xlsx'
                    file.GetContentFile(file_title,
                                        mimetype='application/vnd.openxmlformats-officedocument'
                                                 '.spreadsheetml.sheet')
                    # Download Faculty Load Sheet
                    file_list = drive.ListFile({'q': "title contains 'FacultyLoad' and trashed=false"}).GetList()
                    file_id = file_list[0]['id']
                    file = drive.CreateFile({'id': file_id})
                    file_title = 'UpdatedFacultyLoadSheet.xlsx'
                    file.GetContentFile(file_title,
                                        mimetype='application/vnd.openxmlformats-officedocument'
                                                 '.spreadsheetml.sheet')
                    st.success("Files Downloaded!")

                elif menu == "Add new user":
                    # Action to sign up new user
                    st.subheader("New user registration")
                    new_user = st.text_input("Enter username")
                    new_password = st.text_input("Enter password", type='password')
                    new_ac_type = st.selectbox("Account type", ["Admin", "Faculty"])
                    if new_ac_type == "Faculty":
                        if st.button("Add new faculty"):
                            create_usertable_faculty()
                            add_userdata_faculty(new_user, make_hashes(new_password))
                            st.success("You have successfully created a valid account")
                    elif new_ac_type == "Admin":
                        if st.button("Add new admin"):
                            create_usertable_admin()
                            add_userdata_admin(new_user, make_hashes(new_password))
                            st.success("You have successfully created a valid account")
                elif menu == "Help":
                    st.subheader("Contact details")
            else:
                # If the credentials are wrong
                st.sidebar.warning("Invalid username/password")

    elif ac_type == "Faculty":
        # If account type is faculty, allow only viewing of calendar
        if st.sidebar.checkbox("Login"):
            # Checking credentials
            create_usertable_faculty()
            hashed_password = make_hashes(password)
            result = login_user_faculty(username, check_hashes(password, hashed_password))
            if result:
                # If credentials are correct, display calendar
                st.sidebar.success("Logged in as {}".format(username))
                st.subheader("Faculty view")
                menu = st.selectbox("Menu", ["View calendar", "Download calendar"])
                if menu == "View calendar":
                    month_view = st.selectbox("Select Month", ["Select", "January", "February", "March", "April",
                                                               "May", "June", "July", "August",
                                                               "September", "October", "November", "December"])
                    # Master Calendar fetching and displaying
                    mc = drive.ListFile({'q': "title contains 'Master' and trashed=false"}).GetList()
                    mc_file_id = mc[0]['id']
                    mc_file = drive.CreateFile({'id': mc_file_id})
                    mc_file_title = 'UpdatedMasterCalendar.xlsx'
                    mc_file.GetContentFile(mc_file_title,
                                           mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    if month_view != "Select":
                        st.subheader("Master Calendar")
                        out_stream_mc = xlsx2html(filepath=mc_file_title,
                                                  sheet=month_view,
                                                  output=(os.getcwd() + "/" + mc_file_title + ".html"),
                                                  default_cell_border="10")
                        out_stream_mc.seek(0)
                        html_file_mc = open(mc_file_title + ".html", 'r', encoding='utf-8')
                        source_code_mc = html_file_mc.read()
                        components.html(source_code_mc, height=500, width=700, scrolling=True)

                    # Faculty Calendar fetching and displaying
                    fc = drive.ListFile({'q': "title contains 'FacultyCalendar' and trashed=false"}).GetList()
                    fc_file_id = fc[0]['id']
                    fc_file = drive.CreateFile({'id': fc_file_id})
                    fc_file_title = 'UpdatedFacultyCalendar.xlsx'
                    fc_file.GetContentFile(fc_file_title,
                                           mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    if month_view != "Select":
                        st.subheader("Faculty Calendar")
                        out_stream_fc = xlsx2html(filepath=fc_file_title,
                                                  sheet=month_view,
                                                  output=(os.getcwd() + "/" + fc_file_title + ".html"),
                                                  default_cell_border=10)
                        out_stream_fc.seek(0)
                        html_file_fc = open(fc_file_title + ".html", 'r', encoding='utf-8')
                        source_code_fc = html_file_fc.read()
                        components.html(source_code_fc, height=500, width=700, scrolling=True)

                    # Faculty Loadsheet fetching and displaying
                    fl = drive.ListFile({'q': "title contains 'FacultyLoad' and trashed=false"}).GetList()
                    fl_file_id = fl[0]['id']
                    fl_file = drive.CreateFile({'id': fl_file_id})
                    fl_file_title = 'UpdatedFacultyLoadSheet.xlsx'
                    fl_file.GetContentFile(fl_file_title,
                                           mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    if month_view != "Select":
                        st.subheader("Faculty Loadsheet")
                        out_stream_fl = xlsx2html(filepath=fl_file_title,
                                                  sheet=month_view,
                                                  output=(os.getcwd() + "/" + fl_file_title + ".html"),
                                                  default_cell_border=10)
                        out_stream_fl.seek(0)
                        html_file_fl = open(fl_file_title + ".html", 'r', encoding='utf-8')
                        source_code_fl = html_file_fl.read()
                        components.html(source_code_fl, height=500, width=700, scrolling=True)

                elif menu == "Download calendar":
                    # Downloading master calendar
                    file_list = drive.ListFile({'q': "title contains 'Master' and trashed=false"}).GetList()
                    file_id = file_list[0]['id']
                    file = drive.CreateFile({'id': file_id})
                    file_title = 'UpdatedMasterCalendar.xlsx'
                    file.GetContentFile(file_title, mimetype='application/vnd.openxmlformats-officedocument'
                                                             '.spreadsheetml.sheet')
                    # Download Faculty Calendar
                    file_list = drive.ListFile({'q': "title contains 'FacultyCalendar' and trashed=false"}) \
                        .GetList()
                    file_id = file_list[0]['id']
                    file = drive.CreateFile({'id': file_id})
                    file_title = 'UpdatedFacultyCalendar.xlsx'
                    file.GetContentFile(file_title,
                                        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    # Download Faculty Load Sheet
                    file_list = drive.ListFile({'q': "title contains 'FacultyLoad' and trashed=false"}).GetList()
                    file_id = file_list[0]['id']
                    file = drive.CreateFile({'id': file_id})
                    file_title = 'UpdatedFacultyLoadSheet.xlsx'
                    file.GetContentFile(file_title,
                                        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    st.success("Files Downloaded!")
            else:
                # If the credentials are wrong
                st.sidebar.warning("Invalid username/password")


if __name__ == "__main__":
    main()
