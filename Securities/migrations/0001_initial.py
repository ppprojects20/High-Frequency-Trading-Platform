# Generated by Django 3.0.8 on 2020-09-10 01:04

import Securities.storage
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_date', models.CharField(default='', max_length=60)),
                ('most_active', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='markets_most_active')),
                ('top_gainers', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='markets_top_gainers')),
                ('top_losers', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='markets_top_losers')),
                ('sector_performance', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='markets_sector_performance')),
                ('major_indexes', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='markets_major_indexes')),
                ('upcoming_earnings', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='makets_upcoming_earnings')),
                ('new_ipo', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='markets_new_ipo')),
                ('latest_news', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='markets_news')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='', max_length=10)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('yahoonews', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=500)),
                ('price', models.CharField(blank=True, default='', max_length=500)),
                ('dayLow', models.CharField(blank=True, default='', max_length=500)),
                ('dayHigh', models.CharField(blank=True, default='', max_length=500)),
                ('yearHigh', models.CharField(blank=True, default='', max_length=500)),
                ('yearLow', models.CharField(blank=True, default='', max_length=500)),
                ('priceAvg50', models.CharField(blank=True, default='', max_length=500)),
                ('priceAvg200', models.CharField(blank=True, default='', max_length=500)),
                ('volume', models.CharField(blank=True, default='', max_length=500)),
                ('avgVolume', models.CharField(blank=True, default='', max_length=500)),
                ('openPrice', models.CharField(blank=True, default='', max_length=500)),
                ('previousClose', models.CharField(blank=True, default='', max_length=500)),
                ('eps', models.CharField(blank=True, default='', max_length=500)),
                ('earningsAnnouncement', models.CharField(blank=True, default='', max_length=500)),
                ('sharesOutstanding', models.CharField(blank=True, default='', max_length=500)),
                ('beta', models.CharField(blank=True, default='', max_length=500)),
                ('last_Div', models.CharField(blank=True, default='', max_length=500)),
                ('exchange', models.CharField(blank=True, default='', max_length=500)),
                ('exchangeShortName', models.CharField(blank=True, default='', max_length=500)),
                ('industry', models.CharField(blank=True, default='', max_length=500)),
                ('website', models.URLField(blank=True, default='', null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('ceo', models.CharField(blank=True, default='', max_length=500)),
                ('sector', models.CharField(blank=True, default='', max_length=500)),
                ('country', models.CharField(blank=True, default='', max_length=500)),
                ('fullTimeEmployees', models.CharField(blank=True, default='', max_length=500)),
                ('phone', models.CharField(blank=True, default='', max_length=500)),
                ('address', models.CharField(blank=True, default='', max_length=500)),
                ('city', models.CharField(blank=True, default='', max_length=500)),
                ('state', models.CharField(blank=True, default='', max_length=500)),
                ('zip', models.CharField(blank=True, default='', max_length=500)),
                ('dcfDiff', models.CharField(blank=True, default='', max_length=500)),
                ('dcf', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDate', models.CharField(blank=True, default='', max_length=500)),
                ('rating', models.CharField(blank=True, default='', max_length=500)),
                ('ratingScore', models.CharField(blank=True, default='', max_length=500)),
                ('ratingRecommendation', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsDCFScore', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsDCFRecommendation', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsROEScore', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsROERecommendation', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsROAScore', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsROARecommendation', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsDEScore', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsDERecommendation', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsPEScore', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsPERecommendation', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsPBScore', models.CharField(blank=True, default='', max_length=500)),
                ('ratingDetailsPBRecommendation', models.CharField(blank=True, default='', max_length=500)),
                ('key_executives', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='stock_detail_key_executives')),
                ('stock_logo', models.ImageField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='stocks_logo')),
                ('historicalTimeseries', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='historical_timeseries')),
                ('quarterly_income_statement', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='quarterly_income_stmt')),
                ('annual_income_statement', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='annual_income_stmt')),
                ('quarterly_balance_sheet_statement', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='quarterly_balance_sheet_stmt')),
                ('annual_balance_sheet_statement', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='annual_balance_sheet_stmt')),
                ('quarterly_cash_flow_statement', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='quarterly_cash_flow_stmt')),
                ('annual_cash_flow_statement', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='annual_cash_flow_stmt')),
                ('quarterly_financial_growth', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='quarterly_financial_growth')),
                ('annual_financial_growth', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='annual_financial_growth')),
                ('quarterly_financial_ratio', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='quarterly_financial_ratio')),
                ('annual_financial_ratio', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='annual_financial_ratio')),
                ('quarterly_enterprise_value', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='quarterly_enterprise_value')),
                ('annual_enterprise_value', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='annual_enterprise_value')),
                ('quarterly_key_metrics', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='quarterly_key_metrics')),
                ('annual_key_metrics', models.FileField(blank=True, max_length=500, null=True, storage=Securities.storage.OverwriteStorage(), upload_to='annual_key_metrics')),
            ],
        ),
    ]
