import flask_wtf
from widgets import * #http://wtforms.readthedocs.org/en/latest/fields.html

class Form(flask_wtf.Form):
    name_id = StringField('Name')
    teacher_id = StringField('Teacher')
    #Auton Section
    which_subject = RadioField('Which Subject?',choices=[('English','English'), ('Math','Math'),('Science','Science'),('Social Studies','Social Studies'), ('Art','Art'),('Other','Other')],
                             default='Other')
    like_subject = RadioField('Do you acutally like this subject?', choices=[('0','No'),
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
    rating = RadioField('Please Rate Your Teacher On A Scale Of 1 To 10', choices=[('0','1'),('1','2'),('2','3'),('3','4'),('4','5'),('5','6'),('6','7'),('7','8'),('8','9'),('9','10'),], default='0')
    high_scores = IntegerField('High Goals Scored', default=0, col_sm=6)
    high_misses = IntegerField('High Shots Missed', default=0, col_sm=6)
    low_scores = IntegerField('Low Goals Scored', default=0, col_sm=6)
    fouls = IntegerField('Fouls', default=0, col_sm=6)
    tech_fouls = IntegerField('Tech Fouls', default=0, col_sm=6)

    defense_rating = RadioField('How well did they play defense?', choices=[('0','Did not Defend'), ('1', 'Bad Defense'), ('2', 'Moderate Defense'), ('3', 'Best Defense')], default="0")
    defense_time = RadioField('How much time did they spend on defense?', choices=[('0', 'No Time'), ('1', 'Less than Half'), ('2', 'Most of the Time'), ('3', 'All Match')], default="0")

    hang = CheckboxButtonField('Robot Scaled Tower', col_md=3)
    comments = TextAreaField('How Can We Improve this Survey?', col_lg=12)
