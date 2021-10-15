import argparse
import yaml
import jinja2
from lang import markup


def contains(seq, key):
  return key in seq

def sub(val, fmt):
  return fmt % val

def points(data):
  dom = markup.List(children=map(markup.ListItem, map(parse_line, data['highlights'] if 'highlights' in data else [data['summary']])))
  return convert_markup(dom)

def link(url, label=None, email=False):
  if label is None:
    label = url
  if email:
    url = 'mailto:'+url
  elif '//' not in url:
    url = 'http://'+url
  if args.latex:
    return '\\href{%s}{%s}' % (url, label if label is not None else url)
  else:
    return '<a href="%s" target="%s">%s</a>' % (url, '_top' if email else '_blank', label if label is not None else url)

def linked(data, attr):
  return link(data['website'], data[attr]) if 'website' in data else data[attr]

def convert_attr(obj, attr=None):
  if attr is not None and attr in obj:
    return convert_markup(parse_line(obj[attr]))
  elif attr is None:
    return convert_markup(parse_line(obj))
  else:
    return ''

def parse_line(src):
  assert isinstance(src, str), src
  dom, unparsed = markup.parse_inline(src)
  if unparsed != '':
    raise SyntaxError(unparsed)
  return dom

def convert_markup(dom):
  if args.latex:
    return markup.Latex().convert(dom)
  else:
    return markup.HTML().convert(dom)
  

env = jinja2.Environment(line_statement_prefix='%%', line_comment_prefix='##')
env.tests['contains'] = contains
env.filters['sub'] = sub

env.filters['link'] = link
env.filters['linked'] = linked
env.filters['markup'] = convert_attr

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='A resume template renderer.')
  parser.add_argument('-r', metavar='resume_src', required=True, help='yaml source file for resume')
  parser.add_argument('-t', metavar='template_src', required=True, help='jinja2 source file for template')
  parser.add_argument('-o', metavar='out', help='output filename')
  parser.add_argument('--latex', action='store_true', help='use LaTeX rendering')
  args = parser.parse_args()
  data = yaml.load(open(args.r))
  template = env.from_string(open(args.t).read())
  rendered = template.render(resume=data,
                             points=points,
                             degree=data['education'][0],
                             digits=data['basics']['phone'],
                             links=[data['basics']['website']]+[profile['url'] for profile in data['basics']['profiles']])
  if args.o is None:
    print (rendered)
  else:
    with open(args.o, 'w') as f:
      f.write(rendered)