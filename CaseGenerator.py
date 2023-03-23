# Program for testing around with case numbers for project
# Case Numbers can be seen as: YYYY-CourtAcronym-SixDigitNumber-OptionalLetter
# The dashes in the number are not necessary

# Court acronyms for the majority of cases (prior to Oct. 31, 2022).
court_acronyms_old = ['CA', 'CA1', 'CA2',  # This 'CA' I add due to seeing cases with it, but not in documentation.
                      'CA3', 'CAA', 'CAB',
                      'CAC', 'CAD', 'CAE',
                      'CAF', 'CAH', 'CAL',
                      'CAM', 'CAO', 'CAP',
                      'CAR', 'CAS', 'CAT',
                      'LTB', 'SC1', 'SC2',
                      'SC3', 'SCB', 'SCJ',
                      'FEP', 'ADM', 'DIS',
                      'LIT', 'SEB', 'CVT', 'WIL']

# Court acronyms for newer cases for on or after Oct. 31, 2022.
court_acronyms_new = ['AA', 'AP', 'CAAF', 'CACC', 'CACL', 'CACO',
                      'CAED', 'CAFJ', 'CAFS', 'CAH', 'CAIFJ', 'CAM',
                      'CAQT', 'CAR', 'CARF', 'CAS', 'CAST', 'CAT', 'CATA',
                      'CAVF', 'CTO', 'GC', 'MFLC', 'NCVRA', 'LTNT',
                      'LTR', 'LTPS', 'LTC', 'MFLC', 'COL', 'CTC', 'ED',
                      'FJU', 'INS', 'LTD', 'MAL', 'MFLC', 'PDCTL', 'TOR',
                      'UAA', 'FEP', 'ADM', 'AMC', 'AMF', 'AMP', 'AMS',
                      'AMT', 'NRT', 'DIS', 'LIT', 'SEB', 'CVT', 'WIL']

#  Certified optional letters (by observation) include B, C, M, and L(RB)
optional_letters = ['B', 'C', 'M', 'L(RB)']

# The actual generator. Seems to work. Make a function? Or make case input and data collection function?

# for year in range(1900, 2024):
#     for court in court_acronyms_old:
#         for num in range(0, 1000000):
#             code = str(num)
#             while len(code) < 6:
#                 code = '0' + code
#             if court == 'CA':
#                 for letter in optional_letters:
#                     print(str(year) + court + code + letter)
#             else:
#                 print(str(year) + court + code)


def generate_court_codes(initial_year=1900, end_year=2024):
    for year in range(initial_year, end_year):
        for court in court_acronyms_old:
            for num in range(0, 1000000):
                code = str(num)
                while len(code) < 6:
                    code = '0' + code
                if court == 'CA':
                    for letter in optional_letters:
                        print(str(year) + court + code + letter)
                else:
                    print(str(year) + court + code)
