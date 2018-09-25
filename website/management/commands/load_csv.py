from django.core.management.base import BaseCommand

from django.core.cache import cache

from website.models import Account, Category, Entry, Filter

from django.utils.dateparse import parse_date

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

        # Load up the account
        account = Account.getByName(options['account'])
        if account is None:
            print("Couldn't find account: %s" % options['account'])
            return

        # Load up the csv file
        out = open( options['csv_file'])
        for line in out.readlines():
            data = line.rstrip().split(',')
            date = parse_date(data[1])

            # Create the entry
            entry = Entry.getOrNew(name=data[2],amount=float(data[3]), timestamp=date)

            # Attach a filter
            for filter in filters:
                if re.search(filter.regex, entry.name) is not None:
                    entry.filter = filter
            if entry.filter is None:
                entry.filter = unknown

            # Save the entry out
            entry.save()

