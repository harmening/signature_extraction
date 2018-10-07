import os
from signature_extractor.segmentation import EmailSegmenter
from signature_extractor.preprocessing import mail_parser as m_parser


def print_segments(email_body, signature):
    print("-"*35, "\n", "EMAIL BODY")
    print("_"*35)
    print(email_body)
    print()
    print("-"*35, "\n", "SIGNATURE")
    print("-"*35)
    print(signature)


def main():
    email_fpath = os.path.join('signature_extractor', 'datasets', 'test_emails', 'email_1')
    text = m_parser.get_from_file(email_fpath)

    segmentator_obj = EmailSegmenter()
    email_body, signature = segmentator_obj.segment_mail(text)
    print_segments(email_body, signature)


if __name__ == '__main__':
    main()
