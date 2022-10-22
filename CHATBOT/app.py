{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34552af8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training ai.yml: [#########           ] 44%"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package averaged_perceptron_tagger to\n",
      "[nltk_data]     C:\\Users\\user\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package averaged_perceptron_tagger is already up-to-\n",
      "[nltk_data]       date!\n",
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\user\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n",
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\user\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training ai.yml: [####################] 100%\n",
      "Training botprofile.yml: [####################] 100%\n",
      "Training computers.yml: [####################] 100%\n",
      "Training conversations.yml: [####################] 100%\n",
      "Training emotion.yml: [####################] 100%\n",
      "Training food.yml: [####################] 100%\n",
      "Training gossip.yml: [####################] 100%\n",
      "Training greetings.yml: [####################] 100%\n",
      "Training health.yml: [####################] 100%\n",
      "Training history.yml: [####################] 100%\n",
      "Training humor.yml: [####################] 100%\n",
      "Training literature.yml: [####################] 100%\n",
      "Training money.yml: [####################] 100%\n",
      "Training movies.yml: [####################] 100%\n",
      "Training politics.yml: [####################] 100%\n",
      "Training psychology.yml: [####################] 100%\n",
      "Training science.yml: [####################] 100%\n",
      "Training sports.yml: [####################] 100%\n",
      "Training trivia.yml: [####################] 100%\n",
      " * Serving Flask app '__main__' (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [21/Oct/2022 11:13:50] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [21/Oct/2022 11:13:50] \"GET /static/style.css HTTP/1.1\" 404 -\n",
      "127.0.0.1 - - [21/Oct/2022 11:14:06] \"GET /get?msg=how%20are%20you HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [21/Oct/2022 11:14:16] \"GET /get?msg=are%20you%20sure HTTP/1.1\" 200 -\n",
      "Exception during reset or similar\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\user\\anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\", line 751, in _finalize_fairy\n",
      "    fairy._reset(pool)\n",
      "  File \"C:\\Users\\user\\anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\", line 938, in _reset\n",
      "    pool._dialect.do_rollback(self)\n",
      "  File \"C:\\Users\\user\\anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\default.py\", line 486, in do_rollback\n",
      "    dbapi_connection.rollback()\n",
      "sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 6164 and this is thread id 17604.\n",
      "Exception closing connection <sqlite3.Connection object at 0x00000252295D7C60>\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\user\\anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\", line 751, in _finalize_fairy\n",
      "    fairy._reset(pool)\n",
      "  File \"C:\\Users\\user\\anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\", line 938, in _reset\n",
      "    pool._dialect.do_rollback(self)\n",
      "  File \"C:\\Users\\user\\anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\default.py\", line 486, in do_rollback\n",
      "    dbapi_connection.rollback()\n",
      "sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 6164 and this is thread id 17604.\n",
      "\n",
      "During handling of the above exception, another exception occurred:\n",
      "\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\user\\anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\", line 342, in _close_connection\n",
      "    self._dialect.do_close(connection)\n",
      "  File \"C:\\Users\\user\\anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\default.py\", line 492, in do_close\n",
      "    dbapi_connection.close()\n",
      "sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 6164 and this is thread id 17604.\n",
      "127.0.0.1 - - [21/Oct/2022 11:14:24] \"GET /get?msg=fuck%20you HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [21/Oct/2022 11:14:31] \"GET /get?msg=damn HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [21/Oct/2022 11:14:37] \"GET /get?msg=you HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [21/Oct/2022 11:17:18] \"GET /get?msg=good%20morning HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [21/Oct/2022 11:17:25] \"GET /get?msg=hello HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [21/Oct/2022 11:17:37] \"GET /get?msg=greetings HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [21/Oct/2022 11:17:47] \"GET /get?msg=where%20are%20you HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "#imports\n",
    "from flask import Flask, render_template, request\n",
    "from chatterbot import ChatBot\n",
    "from chatterbot.trainers import ChatterBotCorpusTrainer\n",
    "\n",
    "app = Flask(__name__, template_folder=\"C:/Users/user\")\n",
    "#create chatbot\n",
    "englishBot = ChatBot(\"Chatterbot\", storage_adapter=\"chatterbot.storage.SQLStorageAdapter\")\n",
    "trainer = ChatterBotCorpusTrainer(englishBot)\n",
    "trainer.train(\"chatterbot.corpus.english\") #train the chatter bot for english\n",
    "\n",
    "#define app routes\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "@app.route(\"/get\")\n",
    "#function for the bot response\n",
    "def get_bot_response():\n",
    "    userText = request.args.get('msg')\n",
    "    return str(englishBot.get_response(userText))\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "871f2526",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
