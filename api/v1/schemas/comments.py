#!/usr/bin/env python3
"""Defines request and response schemas for comments endpoints"""


from typing import Dict, Optional
from pydantic import BaseModel


class UpdateComment(BaseModel):
    """Request schema for updating a comment"""
    content: str


class Comment(BaseModel):
    """Defines a comment a comment response"""
    id: str
    content: str
    created_at: str
    updated_at: str
    user: Optional[Dict]


class CommentResponse(BaseModel):
    """Response schema for a comment"""
    success: bool
    status_code: int
    message: str
    data: Comment