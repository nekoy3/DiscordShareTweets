import twint

# Configure
c = twint.Config()
c.Username = "ApexTimes"
c.Search = "【"
c.Limit = 1
c.Output = "get.csv"
c.Lang = "jp"

# Run
twint.run.Search(c)