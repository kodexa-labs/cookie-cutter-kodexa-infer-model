"""Main module."""

from kodexa import Document
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def infer(document: Document):
    logger.info(f"Infer called with document: {document.uuid}")
    return document
