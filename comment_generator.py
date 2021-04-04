"""
Copyright prolog and class level copyright are included in this utility.
This file is intended for the development of comments.
The user can make changes to the text/prolog-text as appropriate.

This work is licensed under
a Creative Commons Attribution-ShareAlike 3.0 Unported License.
©Thorben, 2021
email: thorbendhaenenstd@gmail.com

This file will create a flask application that displays a web application with the
use of a local database to store data. While the website doesn't require a login,
the login structure is used to let the user agree with the terms before using the tool.

The purpose of the website is to generate comments fast for evaluating other students.
The user has some example comments and requirements but needs to build his own repository
by adding his own comments and requirements.

If the user is going to use this for a university course, then the student needs to be aware
that using your own previous work is considered plagiarism. The user is recommended to
make appropriate changes after the comment is generated.

Using comments from someone else without proper citing is also considered plagiarism.
"""

from flask import Flask, render_template, request, redirect, url_for, session
import dbHelper
import gunicorn

app = Flask(__name__)
# The session object needs a secret key
app.secret_key = "HopKIdf78/*9*PO72xQ89Fg??"


@app.route('/intro', methods=['GET', 'POST'])
def intro():
    """
    This function will create the view of the first page.
    The user is required to agree with all the 'commandments'
    before he can enter the other pages.
    It uses the same structure as a login page.
    """
    if request.method == 'GET':
        return render_template('intro.html')
    elif request.method == 'POST':
        session['sworn'] = True
        return redirect(url_for('main'))


@app.route("/swear_again")
def swear_again():
    """
        This function will bring the user back to the terms.
        It's not really necessary but more for fun.
    """
    session['sworn'] = False
    return redirect(url_for('intro'))


@app.route("/", methods=['GET', 'POST'])
def main():
    """
        The view of the main page is to generate predefined comments.
        It uses the class dbHelper to read all the comments and requirements.
    """
    if not session.get('sworn'):
        # The conditional will check if the user agreed with the commandments.
        return render_template('intro.html')
    else:
        db_object = dbHelper.Main()
        requirements_var = db_object.read_database('requirements')
        return render_template('main.html', requirements=requirements_var)


@app.route("/comments", methods=['GET', 'POST'])
def comments():
    """
        The view is to display all the comments and the possibility
        to remove or update them.
    """
    if not session.get('sworn'):
        # The conditional will check if the user agreed with the commandments.
        return render_template('intro.html')
    else:
        if request.method == 'POST':
            for dic in request.form:
                if dic[0:6] == 'update':
                    request_info = {'template_comment': request.form['template_comment'],
                                    'template_type': request.form['template_type'],
                                    'grade_of_excellence': request.form['grade_of_excellence']}
                    if 'written_assignment' in request.form:
                        request_info['written_assignment'] = True
                    else:
                        request_info['written_assignment'] = False
                    if 'programming_assignment' in request.form:
                        request_info['programming_assignment'] = True
                    else:
                        request_info['programming_assignment'] = False
                    if 'math_assignment' in request.form:
                        request_info['math_assignment'] = True
                    else:
                        request_info['math_assignment'] = False
                    db_obj = dbHelper.Comment(comment_arg=request_info['template_comment'],
                                            type_arg=request_info['template_type'],
                                            written_arg=request_info['written_assignment'],
                                            math_arg=request_info['math_assignment'],
                                            programming_arg=request_info['programming_assignment'],
                                            grade_of_excellence_arg=request_info['grade_of_excellence'])
                    db_obj.update_comment(dic[6:])
                elif dic[0:6] == 'delete':
                    comment_obj = dbHelper.Main()
                    comment_obj.del_comment(id=dic[6:], db_name='comments')
        data = dbHelper.Main().read_database(db_name='comments')
        return render_template('comments.html', data=data)


@app.route("/requirements", methods=['GET', 'POST'])
def requirements():
    """
        The view is to display all the requirements and the possibility
        to remove or update them.
    """
    if not session.get('sworn'):
        # The conditional will check if the user agreed with the commandments.
        return render_template('intro.html')
    else:
        if request.method == 'POST':
            for dic in request.form:
                if dic[0:6] == 'update':
                    request_info = {'requirement': request.form['requirement'], 'best': request.form['best'],
                                    'good': request.form['good'], 'bad': request.form['bad'],
                                    'worst': request.form['worst'],
                                    'type': request.form['type']}
                    if 'written_assignment' in request.form:
                        request_info['written_assignment'] = True
                    else:
                        request_info['written_assignment'] = False
                    if 'programming_assignment' in request.form:
                        request_info['programming_assignment'] = True
                    else:
                        request_info['programming_assignment'] = False
                    if 'math_assignment' in request.form:
                        request_info['math_assignment'] = True
                    else:
                        request_info['math_assignment'] = False
                    db_obj = dbHelper.Requirements(requirement_arg=request_info['requirement'],
                                                 best_arg=request_info['best'],
                                                 good_arg=request_info['good'], bad_arg=request_info['bad'],
                                                 worst_arg=request_info['worst'],
                                                 type_arg=request_info['type'],
                                                 written_arg=request_info['written_assignment'],
                                                 math_arg=request_info['math_assignment'],
                                                 programming_arg=request_info['programming_assignment'])
                    db_obj.update_requirement(dic[6:])
                elif dic[0:6] == 'delete':
                    comment_obj = dbHelper.Main()
                    comment_obj.del_comment(id=dic[6:], db_name='requirements')
        data = dbHelper.Main().read_database(db_name='requirements')
        return render_template('requirements.html', data=data)


@app.route("/templates", methods=['GET', 'POST'])
def templates():
    """
        This view will show the template page. The function will receive data
        and store it in the database.
        The comment form will be stored in the comments table
        The requirement form will be stored in the requirements table.
    """
    if not session.get('sworn'):
        # The conditional will check if the user agreed with the commandments.
        return render_template('intro.html')
    else:
        if request.method == "POST":
            if 'template_comment' in request.form:
                request_info = {'template_comment': request.form['template_comment'],
                                'template_type': request.form['template_type'],
                                'grade_of_excellence': request.form['grade_of_excellence']}
                if 'written_assignment' in request.form:
                    request_info['written_assignment'] = True
                else:
                    request_info['written_assignment'] = False
                if 'programming_assignment' in request.form:
                    request_info['programming_assignment'] = True
                else:
                    request_info['programming_assignment'] = False
                if 'math_assignment' in request.form:
                    request_info['math_assignment'] = True
                else:
                    request_info['math_assignment'] = False
                db_obj = dbHelper.Comment(comment_arg=request_info['template_comment'],
                                        type_arg=request_info['template_type'],
                                        written_arg=request_info['written_assignment'],
                                        math_arg=request_info['math_assignment'],
                                        programming_arg=request_info['programming_assignment'],
                                        grade_of_excellence_arg=request_info['grade_of_excellence'])
                db_obj.add_comment()
            elif 'requirement' in request.form:
                request_info = {'requirement': request.form['requirement'], 'best': request.form['best'],
                                'good': request.form['good'], 'bad': request.form['bad'],
                                'worst': request.form['worst'],
                                'type': request.form['type']}
                if 'written_assignment' in request.form:
                    request_info['written_assignment'] = True
                else:
                    request_info['written_assignment'] = False
                if 'programming_assignment' in request.form:
                    request_info['programming_assignment'] = True
                else:
                    request_info['programming_assignment'] = False
                if 'math_assignment' in request.form:
                    request_info['math_assignment'] = True
                else:
                    request_info['math_assignment'] = False
                db_obj = dbHelper.Requirements(requirement_arg=request_info['requirement'], best_arg=request_info['best'],
                                             good_arg=request_info['good'], bad_arg=request_info['bad'],
                                             worst_arg=request_info['worst'],
                                             type_arg=request_info['type'],
                                             written_arg=request_info['written_assignment'],
                                             math_arg=request_info['math_assignment'],
                                             programming_arg=request_info['programming_assignment'])
                db_obj.add_requirement()
        return render_template('template_comment.html')

@app.route('/script.js')
def main_script():
    """
        This function will render the script that is used for the main and intro view.
         This file needs to be rendered because it contains Jinja2 tags.
    """
    db_object = dbHelper.Main()
    requirements_var = db_object.read_database('requirements')
    comments_var = db_object.read_database('comments')
    # For this page we only need the 'comment', the 'grade of excellence' and the 'type' column.
    comments_dict = {}
    for element in comments_var:
        if element[2] in comments_dict:
            comments_dict[element[2]].append(f"{element[6]}:{element[1]}")
        else:
            comments_dict[element[2]] = [f"{element[6]}:{element[1]}"]

    return render_template('main.js', requirements=requirements_var,
                           comments_dict=comments_dict)

@app.errorhandler(403)
def forbidden(e):
    e_friendly = "a forbidden resource"
    return render_template('error.html', e=e, e_friendly=e_friendly), 403

@app.errorhandler(404)
def not_found(e):
    e_friendly = "chap, you made a mistake typing that URL"
    print(type(e))
    return render_template('error.html', e=e, e_friendly=e_friendly), 404

@app.errorhandler(410)
def gone(e):
    e_friendly = "The page existed but is deleted and sent to Valhalla for all eternity."
    return render_template('error.html', e=e, e_friendly=e_friendly), 410

@app.errorhandler(500)
def internal_server_error(e):
    e_friendly = "'server problems' To be overloaded or not to be overloaded. That's the question."
    return render_template('error.html', e=e, e_friendly=e_friendly), 500


if __name__ == '__main__':
    # The session object needs a secret key
    app.secret_key = "HopKIdf78/*9*PO72xQ89Fg??"
    # Turn debug mode on if you want to troubleshoot.
    app.run(debug=False, port="5555")
