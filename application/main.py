from application import app
from flask import render_template
from flask import url_for

@app.route('/')
def index():
	return render_template("index.html",text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sit amet cursus libero, non luctus nulla. Proin in venenatis tellus. Sed quis neque vitae eros lacinia pharetra. Proin ac erat tristique, venenatis dui id, suscipit velit. Vestibulum ac dignissim augue. Duis pharetra quam sit amet erat bibendum lacinia. Etiam vitae lacinia dui, sit amet bibendum ligula. Etiam et orci nec risus tempor laoreet. Maecenas ultricies ultricies orci, id pulvinar velit porttitor sed. Fusce sodales turpis eget facilisis pharetra. Phasellus sed elementum augue, pharetra adipiscing nisl. Maecenas vel mi quis nisl imperdiet auctor ut vitae augue. In quam nibh, rutrum varius placerat eget, pharetra eget ante. Curabitur laoreet, est vitae imperdiet auctor, enim eros ultrices sem, et convallis lorem dui at lorem. Nulla dictum nulla faucibus lorem dignissim auctor. Nulla facilisi.")