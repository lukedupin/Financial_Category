from django.core.management.base import BaseCommand
from decimal import Decimal
from django.utils.dateparse import parse_date

from website.models import Account, Category, Entry, Filter

import re

class Command(BaseCommand):
    help = 'Load a csv file'

    def add_arguments(self, parser):
        parser.add_argument('account', type=str)
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        # Load up the filters
        filters = []
        unknown = None
        for filter in Filter.objects.all():
            if filter.name.lower() != 'unknown':
                filters.append(filter)
            else:
                unknown = filter

        if unknown is None:
            print("Unknown not found.  We need this")
            return

        # Load up the account
        account = Account.getByName(options['account'])
        if account is None:
            print("Couldn't find account: %s" % options['account'])
            return

        # Load up the csv file
        header = True
        out = open( options['csv_file'])
        for line in out.readlines():
            if header:
                header = False
                continue

            #Grab the data
            line = line.rstrip()
            match = re.search(r'(".*")', line)
            data = line.replace(match[1], 'REPLACE').split(',')

            # Date
            date_split = data[1].split('/')
            date = parse_date("%s-%s-%s" % (date_split[2], date_split[0], date_split[1]))

            # Create the entry
            entry = Entry.getOrNew(account=account,
                                   name=match[1],
                                   amount=Decimal.from_float(float(data[3])),
                                   timestamp=date)

            # Attach a filter
            code = match[1].lower()
            for filter in filters:
                if re.search(filter.regex, code) is not None:
                    entry.filter = filter
            if entry.filter_id == 0 or entry.filter_id is None:
                entry.filter = unknown

            # Save the entry out
            entry.save()

