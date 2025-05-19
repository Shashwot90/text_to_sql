import streamlit as st
import os 
import sqlite3 
from langchain_groq import ChatGroq 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.prompts import ChatPromptTemplate

def get_sql_query_from_text(user_query):
    groq_sys_prompt = ChatPromptTemplate.from_template("""
                    