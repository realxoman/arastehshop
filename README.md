# arastehshop

<br>
<h2>How to Run? </h2>
<br>
  <h3>
  At first, Please download Python from <a href="https://python.org">Python.org</a>
</h3>
<h3>
  create a new virtual environment and activate it.
  <a href="https://realpython.com/python-virtual-environments-a-primer/">How To Create a virtual ENV</a>
</h3>
<br>

<h2>
  install the dependencies:
</h2>
<div class="highlight highlight-source-shell">
  <pre>$ pip install -r requirements.txt</pre>
  <p>If you have any problem in installation you can remove the version (Django==3.3.0 >> To >> Django) and then test to install requirements.</p>
</div>
<br>

<h2>
  create a new sqlite database:
</h2>
<div class="highlight highlight-source-shell">
  <pre>$ python manage.py migrate</pre>
</div>
<br>

<h2>
  run the server:
</h2>
<div class="highlight highlight-source-shell">
  <pre>$ python manage.py runserver</pre>
</div>
<br>

Good Luck :)
