# ---+ Extensions
# ---++ GroupUpdatePlugin
# ---+++ Settings

# **STRING**
# The topic to read group update instructions from.
$Foswiki::cfg{GroupUpdatePlugin}{ConfigTopic} = '';

# **STRING**
# If set, a regular expression to match Web.Topic names. Group
# updating will only be attempted after a save on a matching topic.
# This is basically a way to improve performance of this plugin if
# group update instructions fetch information based only on a small set of
# topics.
$Foswiki::cfg{GroupUpdatePlugin}{SourceTopics} = '';

1;
