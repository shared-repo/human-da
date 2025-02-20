from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import DataRequired

class BoardForm(FlaskForm):
    title = StringField('제목', validators=[DataRequired("제목을 입력하세요")])
    writer = StringField('작성자', validators=[DataRequired("로그인 하세요")])
    content = TextAreaField('내용', validators=[DataRequired("내용을 입력하세요")])