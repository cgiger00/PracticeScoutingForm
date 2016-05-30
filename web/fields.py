import flask_wtf
import datetime
from widgets import * #http://wtforms.readthedocs.org/en/latest/fields.html
class Form(flask_wtf.Form):
    name_id = StringField('Name')
    teacher_id = StringField('Teacher')
    time_id = datetime.date.today()
    #Auton Section
    which_subject = RadioField('Which Subject?',choices=[('English','English'), ('Math','Math'),('Science','Science'),('Social Studies','Social Studies'), ('Art','Art'),('Other','Other')],
                             default='Other')
    like_subject = RadioField('Do you actually like this subject?', choices=[('0','No'),
                                                                   ('1','Yes'),
                                                                   ('2','Maybe')],
                                                                   default='0')
    #Teleop Section

    #Breaching checkboxes
    lb_breach = CheckboxButtonField('Gives too much homework')
    pc_breach = CheckboxButtonField('Too artificial')
    cf_breach = CheckboxButtonField('Is lazy and never grades anything')
    mo_breach = CheckboxButtonField('Grades too hard')
    rp_breach = CheckboxButtonField('Is stupid')
    db_breach = CheckboxButtonField('Loses your work')
    sp_breach = CheckboxButtonField('Spends class time complaining about life')
    rw_breach = CheckboxButtonField('On computer all the time')
    rt_breach = CheckboxButtonField('Is completely irrational')

    #Other
    personality = RadioField('What is your teacher like?', choices=[('0','Amazing'), ('1','Alright'),('2','Meh, could be better'),('3','Bad'),('4','Horrendous'),('5','The Worst Person I know x100 * 2')], default='0')
    rating = SelectField('Please Rate Your Teacher On A Scale Of 1 To 10', choices=[('0','1'),('1','2'),('2','3'),('3','4'),('4','5'),('5','6'),('6','7'),('7','8'),('8','9'),('9','10'),], default='0')
    
    #you in class
    learned = BooleanField('I have learned something in class this year' ,false_values =None)
    time_sleep = SelectField('Time Spent Sleeping', choices=[('0','None'),('1','On occasion'),('2','Most of class'),('3',"lol I don't even attend")], default=0,)
    text = BooleanField('I text/snapchat my friends during class', false_values = None)
    other_work = BooleanField('I do other work in class (i.e. math)', false_values = None)
    
    #tech_fouls = IntegerField('Tech Fouls', default=0, col_sm=6)

    dem_smart = RadioField('Do you think your teacher is good at teaching?', choices=[('0','Yes'),('1','No')],default= '0')

    hang = CheckboxButtonField('I Passed The Class!', col_md=3)
    comments = TextAreaField('', col_lg=12)
