require 'nokogiri'
require 'open-uri'
require 'csv'
require 'pry'

page = Nokogiri::HTML(open('https://colleges.niche.com/arizona-state-university/rankings/'))
overall_grade = page.css('div.overall-grade')[0]["class"].split('-').last


result = page.css('div.ranking-cat')
binding.pry