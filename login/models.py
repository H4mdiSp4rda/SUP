# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from datetime import datetime
# Create your models here.
class Course(models.Model):
    INSTITUTES = [("ISLT","Higher Institute of Languages of Tunis(ISLT)"), 
    ("FSB","Faculty of Sciences of Bizerte(FSB)"), ]

    INFO_SUBJECTS = [("MA","Math"), ("PH","Physics"), ("ML","Math Lab"), ]
    
    LETTRE_SUBJECTS = [("POE","Poetry"), ("SYNTAX","Syntax"), ("STY","Stylistics"), 
    ("AMCIV","American Civilization"), ("LITT","Lit Theory"), ]

    title         = models.CharField(max_length=120, blank=True, null=True)
    course        = models.FileField(blank=True, null=True)
    institute     = models.CharField(max_length=120, choices= INSTITUTES)
    subject       = models.CharField(max_length=120, choices= LETTRE_SUBJECTS)
    description   = models.TextField(max_length=1000, blank=True, null=True)
    added         = models.DateTimeField(auto_now_add=True, )
    updated       = models.DateTimeField(auto_now=True, )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse