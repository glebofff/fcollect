# Generated by Django 2.2 on 2019-12-09 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.DateTimeField(db_index=True)),
                ('code', models.CharField(choices=[('AED', 'United Arab Emirates Dirham'), ('AFN', 'Afghanistan Afghani'), ('ALL', 'Albania Lek'), ('AMD', 'Armenia Dram'), ('ANG', 'Netherlands Antilles Guilder'), ('AOA', 'Angola Kwanza'), ('ARS', 'Argentina Peso'), ('AUD', 'Australia Dollar'), ('AWG', 'Aruba Guilder'), ('AZN', 'Azerbaijan New Manat'), ('BAM', 'Bosnia and Herzegovina Convertible Marka'), ('BBD', 'Barbados Dollar'), ('BDT', 'Bangladesh Taka'), ('BGN', 'Bulgaria Lev'), ('BHD', 'Bahrain Dinar'), ('BIF', 'Burundi Franc'), ('BMD', 'Bermuda Dollar'), ('BND', 'Brunei Darussalam Dollar'), ('BOB', 'Bolivia Bolíviano'), ('BRL', 'Brazil Real'), ('BSD', 'Bahamas Dollar'), ('BTN', 'Bhutan Ngultrum'), ('BWP', 'Botswana Pula'), ('BYR', 'Belarus Ruble'), ('BZD', 'Belize Dollar'), ('CAD', 'Canada Dollar'), ('CDF', 'Congo/Kinshasa Franc'), ('CHF', 'Switzerland Franc'), ('CLP', 'Chile Peso'), ('CNY', 'China Yuan Renminbi'), ('COP', 'Colombia Peso'), ('CRC', 'Costa Rica Colon'), ('CUC', 'Cuba Convertible Peso'), ('CUP', 'Cuba Peso'), ('CVE', 'Cape Verde Escudo'), ('CZK', 'Czech Republic Koruna'), ('DJF', 'Djibouti Franc'), ('DKK', 'Denmark Krone'), ('DOP', 'Dominican Republic Peso'), ('DZD', 'Algeria Dinar'), ('EGP', 'Egypt Pound'), ('ERN', 'Eritrea Nakfa'), ('ETB', 'Ethiopia Birr'), ('EUR', 'Euro Member Countries'), ('FJD', 'Fiji Dollar'), ('FKP', 'Falkland Islands (Malvinas) Pound'), ('GBP', 'United Kingdom Pound'), ('GEL', 'Georgia Lari'), ('GGP', 'Guernsey Pound'), ('GHS', 'Ghana Cedi'), ('GIP', 'Gibraltar Pound'), ('GMD', 'Gambia Dalasi'), ('GNF', 'Guinea Franc'), ('GTQ', 'Guatemala Quetzal'), ('GYD', 'Guyana Dollar'), ('HKD', 'Hong Kong Dollar'), ('HNL', 'Honduras Lempira'), ('HRK', 'Croatia Kuna'), ('HTG', 'Haiti Gourde'), ('HUF', 'Hungary Forint'), ('IDR', 'Indonesia Rupiah'), ('ILS', 'Israel Shekel'), ('IMP', 'Isle of Man Pound'), ('INR', 'India Rupee'), ('IQD', 'Iraq Dinar'), ('IRR', 'Iran Rial'), ('ISK', 'Iceland Krona'), ('JEP', 'Jersey Pound'), ('JMD', 'Jamaica Dollar'), ('JOD', 'Jordan Dinar'), ('JPY', 'Japan Yen'), ('KES', 'Kenya Shilling'), ('KGS', 'Kyrgyzstan Som'), ('KHR', 'Cambodia Riel'), ('KMF', 'Comoros Franc'), ('KPW', 'Korea (North) Won'), ('KRW', 'Korea (South) Won'), ('KWD', 'Kuwait Dinar'), ('KYD', 'Cayman Islands Dollar'), ('KZT', 'Kazakhstan Tenge'), ('LAK', 'Laos Kip'), ('LBP', 'Lebanon Pound'), ('LKR', 'Sri Lanka Rupee'), ('LRD', 'Liberia Dollar'), ('LSL', 'Lesotho Loti'), ('LYD', 'Libya Dinar'), ('MAD', 'Morocco Dirham'), ('MDL', 'Moldova Leu'), ('MGA', 'Madagascar Ariary'), ('MKD', 'Macedonia Denar'), ('MMK', 'Myanmar (Burma) Kyat'), ('MNT', 'Mongolia Tughrik'), ('MOP', 'Macau Pataca'), ('MRO', 'Mauritania Ouguiya'), ('MUR', 'Mauritius Rupee'), ('MVR', 'Maldives (Maldive Islands) Rufiyaa'), ('MWK', 'Malawi Kwacha'), ('MXN', 'Mexico Peso'), ('MYR', 'Malaysia Ringgit'), ('MZN', 'Mozambique Metical'), ('NAD', 'Namibia Dollar'), ('NGN', 'Nigeria Naira'), ('NIO', 'Nicaragua Cordoba'), ('NOK', 'Norway Krone'), ('NPR', 'Nepal Rupee'), ('NZD', 'New Zealand Dollar'), ('OMR', 'Oman Rial'), ('PAB', 'Panama Balboa'), ('PEN', 'Peru Sol'), ('PGK', 'Papua New Guinea Kina'), ('PHP', 'Philippines Peso'), ('PKR', 'Pakistan Rupee'), ('PLN', 'Poland Zloty'), ('PYG', 'Paraguay Guarani'), ('QAR', 'Qatar Riyal'), ('RON', 'Romania New Leu'), ('RSD', 'Serbia Dinar'), ('RUB', 'Russia Ruble'), ('RWF', 'Rwanda Franc'), ('SAR', 'Saudi Arabia Riyal'), ('SBD', 'Solomon Islands Dollar'), ('SCR', 'Seychelles Rupee'), ('SDG', 'Sudan Pound'), ('SEK', 'Sweden Krona'), ('SGD', 'Singapore Dollar'), ('SHP', 'Saint Helena Pound'), ('SLL', 'Sierra Leone Leone'), ('SOS', 'Somalia Shilling'), ('SPL', 'Seborga Luigino'), ('SRD', 'Suriname Dollar'), ('STD', 'São Tomé and Príncipe Dobra'), ('SVC', 'El Salvador Colon'), ('SYP', 'Syria Pound'), ('SZL', 'Swaziland Lilangeni'), ('THB', 'Thailand Baht'), ('TJS', 'Tajikistan Somoni'), ('TMT', 'Turkmenistan Manat'), ('TND', 'Tunisia Dinar'), ('TOP', "Tonga Pa'anga"), ('TRY', 'Turkey Lira'), ('TTD', 'Trinidad and Tobago Dollar'), ('TVD', 'Tuvalu Dollar'), ('TWD', 'Taiwan New Dollar'), ('TZS', 'Tanzania Shilling'), ('UAH', 'Ukraine Hryvnia'), ('UGX', 'Uganda Shilling'), ('USD', 'United States Dollar'), ('UYU', 'Uruguay Peso'), ('UZS', 'Uzbekistan Som'), ('VEF', 'Venezuela Bolivar'), ('VND', 'Viet Nam Dong'), ('VUV', 'Vanuatu Vatu'), ('WST', 'Samoa Tala'), ('XAF', 'Communauté Financière Africaine (BEAC) CFA Franc BEAC'), ('XCD', 'East Caribbean Dollar'), ('XDR', 'International Monetary Fund (IMF) Special Drawing Rights'), ('XOF', 'Communauté Financière Africaine (BCEAO) Franc'), ('XPF', 'Comptoirs Français du Pacifique (CFP) Franc'), ('YER', 'Yemen Rial'), ('ZAR', 'South Africa Rand'), ('ZMW', 'Zambia Kwacha'), ('ZWD', 'Zimbabwe Dollar')], db_index=True, max_length=3)),
                ('rate', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='RateSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbr', models.CharField(db_index=True, max_length=64)),
                ('last_poll', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='ratesource',
            constraint=models.UniqueConstraint(fields=('abbr',), name='rate_source_unique_abbr_cst'),
        ),
        migrations.AddField(
            model_name='ratelog',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currencies.RateSource'),
        ),
        migrations.AddField(
            model_name='ratelog',
            name='base',
            field=models.CharField(choices=[('AED', 'United Arab Emirates Dirham'), ('AFN', 'Afghanistan Afghani'), ('ALL', 'Albania Lek'), ('AMD', 'Armenia Dram'), ('ANG', 'Netherlands Antilles Guilder'), ('AOA', 'Angola Kwanza'), ('ARS', 'Argentina Peso'), ('AUD', 'Australia Dollar'), ('AWG', 'Aruba Guilder'), ('AZN', 'Azerbaijan New Manat'), ('BAM', 'Bosnia and Herzegovina Convertible Marka'), ('BBD', 'Barbados Dollar'), ('BDT', 'Bangladesh Taka'), ('BGN', 'Bulgaria Lev'), ('BHD', 'Bahrain Dinar'), ('BIF', 'Burundi Franc'), ('BMD', 'Bermuda Dollar'), ('BND', 'Brunei Darussalam Dollar'), ('BOB', 'Bolivia Bolíviano'), ('BRL', 'Brazil Real'), ('BSD', 'Bahamas Dollar'), ('BTN', 'Bhutan Ngultrum'), ('BWP', 'Botswana Pula'), ('BYR', 'Belarus Ruble'), ('BZD', 'Belize Dollar'), ('CAD', 'Canada Dollar'), ('CDF', 'Congo/Kinshasa Franc'), ('CHF', 'Switzerland Franc'), ('CLP', 'Chile Peso'), ('CNY', 'China Yuan Renminbi'), ('COP', 'Colombia Peso'), ('CRC', 'Costa Rica Colon'), ('CUC', 'Cuba Convertible Peso'), ('CUP', 'Cuba Peso'), ('CVE', 'Cape Verde Escudo'), ('CZK', 'Czech Republic Koruna'), ('DJF', 'Djibouti Franc'), ('DKK', 'Denmark Krone'), ('DOP', 'Dominican Republic Peso'), ('DZD', 'Algeria Dinar'), ('EGP', 'Egypt Pound'), ('ERN', 'Eritrea Nakfa'), ('ETB', 'Ethiopia Birr'), ('EUR', 'Euro Member Countries'), ('FJD', 'Fiji Dollar'), ('FKP', 'Falkland Islands (Malvinas) Pound'), ('GBP', 'United Kingdom Pound'), ('GEL', 'Georgia Lari'), ('GGP', 'Guernsey Pound'), ('GHS', 'Ghana Cedi'), ('GIP', 'Gibraltar Pound'), ('GMD', 'Gambia Dalasi'), ('GNF', 'Guinea Franc'), ('GTQ', 'Guatemala Quetzal'), ('GYD', 'Guyana Dollar'), ('HKD', 'Hong Kong Dollar'), ('HNL', 'Honduras Lempira'), ('HRK', 'Croatia Kuna'), ('HTG', 'Haiti Gourde'), ('HUF', 'Hungary Forint'), ('IDR', 'Indonesia Rupiah'), ('ILS', 'Israel Shekel'), ('IMP', 'Isle of Man Pound'), ('INR', 'India Rupee'), ('IQD', 'Iraq Dinar'), ('IRR', 'Iran Rial'), ('ISK', 'Iceland Krona'), ('JEP', 'Jersey Pound'), ('JMD', 'Jamaica Dollar'), ('JOD', 'Jordan Dinar'), ('JPY', 'Japan Yen'), ('KES', 'Kenya Shilling'), ('KGS', 'Kyrgyzstan Som'), ('KHR', 'Cambodia Riel'), ('KMF', 'Comoros Franc'), ('KPW', 'Korea (North) Won'), ('KRW', 'Korea (South) Won'), ('KWD', 'Kuwait Dinar'), ('KYD', 'Cayman Islands Dollar'), ('KZT', 'Kazakhstan Tenge'), ('LAK', 'Laos Kip'), ('LBP', 'Lebanon Pound'), ('LKR', 'Sri Lanka Rupee'), ('LRD', 'Liberia Dollar'), ('LSL', 'Lesotho Loti'), ('LYD', 'Libya Dinar'), ('MAD', 'Morocco Dirham'), ('MDL', 'Moldova Leu'), ('MGA', 'Madagascar Ariary'), ('MKD', 'Macedonia Denar'), ('MMK', 'Myanmar (Burma) Kyat'), ('MNT', 'Mongolia Tughrik'), ('MOP', 'Macau Pataca'), ('MRO', 'Mauritania Ouguiya'), ('MUR', 'Mauritius Rupee'), ('MVR', 'Maldives (Maldive Islands) Rufiyaa'), ('MWK', 'Malawi Kwacha'), ('MXN', 'Mexico Peso'), ('MYR', 'Malaysia Ringgit'), ('MZN', 'Mozambique Metical'), ('NAD', 'Namibia Dollar'), ('NGN', 'Nigeria Naira'), ('NIO', 'Nicaragua Cordoba'), ('NOK', 'Norway Krone'), ('NPR', 'Nepal Rupee'), ('NZD', 'New Zealand Dollar'), ('OMR', 'Oman Rial'), ('PAB', 'Panama Balboa'), ('PEN', 'Peru Sol'), ('PGK', 'Papua New Guinea Kina'), ('PHP', 'Philippines Peso'), ('PKR', 'Pakistan Rupee'), ('PLN', 'Poland Zloty'), ('PYG', 'Paraguay Guarani'), ('QAR', 'Qatar Riyal'), ('RON', 'Romania New Leu'), ('RSD', 'Serbia Dinar'), ('RUB', 'Russia Ruble'), ('RWF', 'Rwanda Franc'), ('SAR', 'Saudi Arabia Riyal'), ('SBD', 'Solomon Islands Dollar'), ('SCR', 'Seychelles Rupee'), ('SDG', 'Sudan Pound'), ('SEK', 'Sweden Krona'), ('SGD', 'Singapore Dollar'), ('SHP', 'Saint Helena Pound'), ('SLL', 'Sierra Leone Leone'), ('SOS', 'Somalia Shilling'), ('SPL', 'Seborga Luigino'), ('SRD', 'Suriname Dollar'), ('STD', 'São Tomé and Príncipe Dobra'), ('SVC', 'El Salvador Colon'), ('SYP', 'Syria Pound'), ('SZL', 'Swaziland Lilangeni'), ('THB', 'Thailand Baht'), ('TJS', 'Tajikistan Somoni'), ('TMT', 'Turkmenistan Manat'), ('TND', 'Tunisia Dinar'), ('TOP', "Tonga Pa'anga"), ('TRY', 'Turkey Lira'), ('TTD', 'Trinidad and Tobago Dollar'), ('TVD', 'Tuvalu Dollar'), ('TWD', 'Taiwan New Dollar'), ('TZS', 'Tanzania Shilling'), ('UAH', 'Ukraine Hryvnia'), ('UGX', 'Uganda Shilling'), ('USD', 'United States Dollar'), ('UYU', 'Uruguay Peso'), ('UZS', 'Uzbekistan Som'), ('VEF', 'Venezuela Bolivar'), ('VND', 'Viet Nam Dong'), ('VUV', 'Vanuatu Vatu'), ('WST', 'Samoa Tala'), ('XAF', 'Communauté Financière Africaine (BEAC) CFA Franc BEAC'), ('XCD', 'East Caribbean Dollar'), ('XDR', 'International Monetary Fund (IMF) Special Drawing Rights'), ('XOF', 'Communauté Financière Africaine (BCEAO) Franc'), ('XPF', 'Comptoirs Français du Pacifique (CFP) Franc'), ('YER', 'Yemen Rial'), ('ZAR', 'South Africa Rand'), ('ZMW', 'Zambia Kwacha'), ('ZWD', 'Zimbabwe Dollar')], db_index=True, default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='ratesource',
            name='last_poll',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='ratesource',
            name='remote_ts',
            field=models.DateTimeField(null=True),
        ),
    ]
