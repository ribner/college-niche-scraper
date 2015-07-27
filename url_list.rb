require 'nokogiri'
require 'open-uri'
require 'csv'
setting = false
link_list = []
link_endings = %w(3-A B C D E F G H I J K L M N O P Q-R S T U V W X-Z )




link_endings.each do |ending|
	sleep(2)
	page = Nokogiri::HTML(open("https://colleges.niche.com/all/?LetterGroup="+ending))
	page.css('li').css('a').each do |element|
		
		link = element['href']
		if link == '/rankings/best-overall/'
			setting = false
		end	
		if setting == true
			link_list << link
		end
		if link == '/all/?LetterGroup=X-Z'
			setting = true
		end
	end
end

CSV.open("college-niche.csv", "wb") do |csv|
	link_list.each do |element|
		csv << ['https://colleges.niche.com' + element + 'rankings/']
	end
end