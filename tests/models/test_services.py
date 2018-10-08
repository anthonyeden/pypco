"""Tests for the Services model classes."""

#pylint: disable=E1101

import unittest
from requests import HTTPError
from .. import BasePCOVCRTestCase
import pypco

class TestServices(BasePCOVCRTestCase):
    """Test the Services model classes."""

    def test_list_arrangement_sections(self):
        """Verify that we can list arrangement sections."""

        pco = self.pco

        song = pco.services.songs.get("16194010")
        arrangement = [arr for arr in song.rel.arrangements.list()][0]

        sections = [sec for sec in arrangement.rel.sections.list()]

        self.assertEqual(len(sections), 1)
        self.assertEqual(sections[0].sections[0]['label'], 'Verse 1')

    def test_list_media(self):
        """Verify that we can list media."""

        pco = self.pco

        image = [media for media in pco.services.media.list()][0]

        self.assertIsInstance(image, pypco.models.services.Media)
        self.assertEqual(image.title, 'Field Image')
        self.assertEqual(image.media_type_name, 'Background Image')

    def test_attachment_activity(self):
        """Test attachment activities--opening and previewing."""

        pco = self.pco

        image = [media for media in pco.services.media.list()][0]

        self.assertIsInstance(image, pypco.models.services.Media)
        self.assertEqual(image.title, 'Field Image')
        self.assertEqual(image.media_type_name, 'Background Image')

        attachment = [attachment for attachment in image.rel.attachments.list()][0]

        attach_open = attachment.open()
        self.assertIsInstance(attach_open, pypco.models.services.AttachmentActivity)
        self.assertEqual('open', attach_open.activity_type)
        self.assertIsInstance(attach_open.attachment_url, str)

        attach_preview = attachment.preview()
        self.assertIsInstance(attach_preview, pypco.models.services.AttachmentActivity)
        self.assertEqual('preview', attach_preview.activity_type)
        self.assertIsInstance(attach_preview.attachment_url, str)
