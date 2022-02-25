from pymol import cmd, stored

def ReprBindingPocket(prot):
    cmd.extract('lig', 'organic')
    cmd.extract('prot', 'polymer')
    cmd.delete(prot)

    cmd.set('surface_carve_cutoff', 4.5)
    cmd.set('surface_carve_selection', 'lig')
    cmd.set('surface_carve_normal_cutoff', -0.1)
    cmd.hide('everything', 'prot')
    cmd.show('lines', 'prot')

    cmd.show('surface', 'prot within 8 of lig')
    cmd.set('two_sided_lighting')
    cmd.set('transparency', 0.5)
    cmd.show('sticks', 'lig')
    cmd.orient('lig')

    cmd.set('surface_color', 'white')
    cmd.set('surface_type', 2)
    cmd.unset('ray_shadows')

cmd.extend( 'ReprBindingPocket', ReprBindingPocket ) 