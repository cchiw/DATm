/*---------- begin exec-head.in ----------*/
/*! \file symb_fsd2_sym.cxx
 *
 * Generated from symb_fsd2_sym.diderot.
 *
 * Command: /Users/chariseechiw/diderot/vis15/bin/diderotc --exec symb_fsd2_sym.diderot
 * Version: vis15:2016-07-29
 */
/*---------- end exec-head.in ----------*/

#define DIDEROT_STRAND_ARRAY
/*---------- begin exec-incl.in ----------*/
#define DIDEROT_STANDALONE_EXEC
#define DIDEROT_SINGLE_PRECISION
#define DIDEROT_INT
#define DIDEROT_TARGET_SEQUENTIAL
#include "diderot/diderot.hxx"
/*---------- end exec-incl.in ----------*/

// ***** Begin synthesized types *****

namespace Diderot {
    typedef float vec2 __attribute__ ((vector_size (8)));
    struct tensor_ref_2 : public diderot::tensor_ref<float,2> {
        tensor_ref_2 (const float *src);
        tensor_ref_2 (struct tensor_2 const & ten);
        tensor_ref_2 (tensor_ref_2 const & ten);
    };
    struct tensor_ref_4 : public diderot::tensor_ref<float,4> {
        tensor_ref_4 (const float *src);
        tensor_ref_4 (struct tensor_4 const & ten);
        tensor_ref_4 (tensor_ref_4 const & ten);
    };
    struct tensor_4 : public diderot::tensor<float,4> {
        tensor_4 ()
            : diderot::tensor<float,4>()
        { }
        tensor_4 (std::initializer_list< float > const & il)
            : diderot::tensor<float,4>(il)
        { }
        tensor_4 (const float *src)
            : diderot::tensor<float,4>(src)
        { }
        tensor_4 (tensor_4 const & ten)
            : diderot::tensor<float,4>(ten._data)
        { }
        ~tensor_4 () { }
        tensor_4 & operator= (tensor_4 const & src);
        tensor_4 & operator= (tensor_ref_4 const & src);
        tensor_4 & operator= (std::initializer_list< float > const & il);
        tensor_4 & operator= (const float *src);
    };
    struct tensor_2 : public diderot::tensor<float,2> {
        tensor_2 ()
            : diderot::tensor<float,2>()
        { }
        tensor_2 (std::initializer_list< float > const & il)
            : diderot::tensor<float,2>(il)
        { }
        tensor_2 (const float *src)
            : diderot::tensor<float,2>(src)
        { }
        tensor_2 (tensor_2 const & ten)
            : diderot::tensor<float,2>(ten._data)
        { }
        ~tensor_2 () { }
        tensor_2 & operator= (tensor_2 const & src);
        tensor_2 & operator= (tensor_ref_2 const & src);
        tensor_2 & operator= (std::initializer_list< float > const & il);
        tensor_2 & operator= (const float *src);
    };
    inline tensor_ref_2::tensor_ref_2 (const float *src)
        : diderot::tensor_ref<float,2>(src)
    { }
    inline tensor_ref_2::tensor_ref_2 (struct tensor_2 const & ten)
        : diderot::tensor_ref<float,2>(ten._data)
    { }
    inline tensor_ref_2::tensor_ref_2 (tensor_ref_2 const & ten)
        : diderot::tensor_ref<float,2>(ten._data)
    { }
    inline tensor_ref_4::tensor_ref_4 (const float *src)
        : diderot::tensor_ref<float,4>(src)
    { }
    inline tensor_ref_4::tensor_ref_4 (struct tensor_4 const & ten)
        : diderot::tensor_ref<float,4>(ten._data)
    { }
    inline tensor_ref_4::tensor_ref_4 (tensor_ref_4 const & ten)
        : diderot::tensor_ref<float,4>(ten._data)
    { }
    inline tensor_4 & tensor_4::operator= (tensor_4 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_4 & tensor_4::operator= (tensor_ref_4 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_4 & tensor_4::operator= (std::initializer_list< float > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_4 & tensor_4::operator= (const float *src)
    {
        this->copy(src);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (tensor_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (tensor_ref_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (std::initializer_list< float > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (const float *src)
    {
        this->copy(src);
        return *this;
    }
} // namespace Diderot
// ***** End synthesized types *****

/*---------- begin namespace-open.in ----------*/
namespace Diderot {

static std::string ProgramName = "symb_fsd2_sym";

struct world;
struct sample_strand;
/*---------- end namespace-open.in ----------*/

/*---------- begin nrrd-save-helper.in ----------*/
/* helper function for saving output to nrrd file */
inline bool nrrd_save_helper (
        std::string const &stem,
        std::string const &suffix,
        std::string const &ext,
        Nrrd *nrrd)
{
    std::string file = stem + suffix + "." + ext;
    if (nrrdSave (file.c_str(), nrrd, nullptr)) {
        std::cerr << "Error saving \"" << file << "\":\n" << biffGetDone(NRRD) << std::endl;
        return true;
    }
    else {
        return false;
    }
}
/*---------- end nrrd-save-helper.in ----------*/

struct globals {
    int32_t gv_sz0;
    int32_t gv_sz1;
    float gv_width;
    tensor_2 gv_off;
    float gv_shear;
    float gv_angle;
    tensor_4 gv_parm;
    tensor_2 gv_edge0;
    tensor_2 gv_edge1;
    tensor_2 gv_orig;
};
struct sample_strand {
    float sv_out;
    int32_t sv_idx0;
    int32_t sv_idx1;
};
/*---------- begin seq-sarr.in ----------*/
// forward declarations of strand methods
#ifdef DIDEROT_HAS_START_METHOD
static diderot::strand_status sample_start (sample_strand *self);
#endif // DIDEROT_HAS_START_METHOD
static diderot::strand_status sample_update (world *wrld, globals *glob, sample_strand *self);
#ifdef DIDEROT_HAS_STABILIZE_METHOD
static void sample_stabilize (sample_strand *self);
#endif // DIDEROT_HAS_STABILIZE_METHOD

// strand_array for SEQUENTIAL/NO BSP/SINGLE STATE/DIRECT ACCESS
//
struct strand_array {
    typedef sample_strand strand_t;
    typedef uint32_t index_t;
    typedef index_t sid_t;              // strand ID (index into strand-state storage)

    uint8_t             *_status;       // the array of status information for the strands
    char                *_storage;      // points to array of sample_strand structs
    uint32_t            _nItems;        // number of items in the _storage and _status arrays
    uint32_t            _nStable;       // number of stable strands
    uint32_t            _nActive;       // number of active strands
    uint32_t		_nFresh;	// number of fresh strands (new strands from create_strands)

    strand_array () : _status(nullptr), _storage(nullptr), _nItems(0) { }
    ~strand_array ();

    uint32_t in_state_index () const { return 0; /* dummy */ }

    uint32_t num_active () const { return this->_nActive; }
    uint32_t num_stable () const { return this->_nStable; }
    uint32_t num_alive () const { return this->_nActive+this->_nStable; }

  // return the ID of a strand, which is the same as the ix index
    sid_t id (index_t ix) const
    {
        assert (ix < this->_nItems);
        return ix;
    }
  // return a pointer to the strand with the given ID
    sample_strand *id_to_strand (sid_t id) const
    {
        assert (id < this->_nItems);
        return reinterpret_cast<sample_strand *>(this->_storage + id * sizeof(sample_strand));
    }

  // return a strand's status
    diderot::strand_status status (index_t ix) const
    {
        assert (ix < this->_nItems);
        return static_cast<diderot::strand_status>(this->_status[ix]);
    }
  // return a pointer to the given strand
    sample_strand *strand (index_t ix) const
    {
        return this->id_to_strand(this->id(ix));
    }
  // return a pointer to the local state of strand ix
    sample_strand *local_state (index_t ix) const
    {
        return this->strand(ix);
    }
  // return a pointer to the local state of strand with the given ID
    sample_strand *id_to_local_state (sid_t id) const
    {
        return this->id_to_strand(id);
    }

  // allocate space for nItems
    bool alloc (uint32_t nItems)
    {
        this->_storage = static_cast<char *>(std::malloc (nItems * sizeof(sample_strand)));
        if (this->_storage == nullptr) {
            return true;
        }
        this->_status = static_cast<uint8_t *>(std::malloc (nItems * sizeof(uint8_t)));
        if (this->_status == nullptr) {
            std::free (this->_storage);
            return true;
        }
        this->_nItems = nItems;
        this->_nActive = 0;
        this->_nStable = 0;
        this->_nFresh = 0;
        return false;
    }

  // initialize the first nStrands locations as new active strands
    void create_strands (uint32_t nStrands)
    {
        assert (this->_nActive == 0);
        assert (this->_nItems == nStrands);
        for (index_t ix = 0;  ix < nStrands;  ix++) {
            this->_status[ix] = diderot::kActive;
            new (this->strand(ix)) sample_strand;
        }
        this->_nActive = nStrands;
        this->_nFresh = nStrands;
    }

  // swap in and out states (NOP for this version)
    void swap () { }

#ifdef DIDEROT_HAS_START_METHOD
  // invoke strand's start method
    diderot::strand_status strand_start (index_t ix)
    {
        return sample_start(this->strand(ix));
    }
#endif // DIDEROT_HAS_START_METHOD

  // invoke strand's update method
    diderot::strand_status strand_update (world *wrld, globals *glob, index_t ix)
    {
        return sample_update(wrld, glob, this->strand(ix));
    }

  // invoke strand's stabilize method
    index_t strand_stabilize (index_t ix)
    {
#ifdef DIDEROT_HAS_STABILIZE_METHOD
        sample_stabilize (this->strand(ix));
#endif // DIDEROT_HAS_STABILIZE_METHOD
        this->_status[ix] = diderot::kStable;
        this->_nActive--;
        this->_nStable++;
      // skip to next active strand
	do {
	    ix++;
        } while ((ix < this->_nItems) && (this->_status[ix] != diderot::kActive));
	return ix;
    }

  // mark the given strand as dead
    index_t kill (index_t ix)
    {
        this->_status[ix] = diderot::kDead;
        this->_nActive--;
      // skip to next active strand
	do {
	    ix++;
        } while ((ix < this->_nItems) && (this->_status[ix] != diderot::kActive));
	return ix;
    }

  // finish the local-phase of a superstep (NOP)
    void finish_step () { }

  // finish a kill_all operation (NOP)
    void finish_kill_all () { }

  // finish a stabilize_all operation (NOP)
    void finish_stabilize_all () { }

    index_t begin_alive () const
    {
        index_t ix = 0;
#ifdef DIDEROT_HAS_STRAND_DIE
        while ((ix < this->_nItems) && (this->_status[ix] == diderot::kDead)) {
            ix++;
        }
#endif
        return ix;
    }
    index_t end_alive () const { return this->_nItems; }
    index_t next_alive (index_t &ix) const
    {
        ix++;
#ifdef DIDEROT_HAS_STRAND_DIE
        while ((ix < this->_nItems) && (this->_status[ix] == diderot::kDead)) {
            ix++;
        }
#endif
        return ix;
    }

  // iterator over active strands
    index_t begin_active () const
    {
        index_t ix = 0;
        while ((ix < this->_nItems) && (this->_status[ix] != diderot::kActive)) {
            ix++;
        }
        return ix;
    }
    index_t end_active () const { return this->_nItems; }
    index_t next_active (index_t &ix) const
    {
	do {
	    ix++;
        } while ((ix < this->_nItems) && (this->_status[ix] != diderot::kActive));
        return ix;
    }

  // iterator over stable strands
    index_t begin_stable () const
    {
        index_t ix = 0;
        while ((ix < this->_nItems) && (this->_status[ix] != diderot::kStable)) {
            ix++;
        }
        return ix;
    }
    index_t end_stable () const { return this->_nItems; }
    index_t next_stable (index_t &ix) const
    {
	do {
	    ix++;
        } while ((ix < this->_nItems) && (this->_status[ix] != diderot::kStable));
        return ix;
    }

  // iterator over fresh strands; since the only new strands were created by create_strand
  // we iterate over all of them
    index_t begin_fresh () const { return 0; }
    index_t end_fresh () const { return this->_nFresh; }
    index_t next_fresh (index_t &ix) const { return ++ix; }

}; // struct strand_array

strand_array::~strand_array ()
{
  // run destructors to reclaim any dynamic memory attached to the strand state
    for (auto ix = this->begin_alive();  ix != this->end_alive();  ix = this->next_alive(ix)) {
        this->strand(ix)->~sample_strand();
    }
    if (this->_status != nullptr) std::free (this->_status);
    if (this->_storage != nullptr) std::free (this->_storage);
}
/*---------- end seq-sarr.in ----------*/

struct world : public diderot::world_base {
    strand_array _strands;
    globals *_globals;
    world ();
    ~world ();
    bool init ();
    bool alloc (int32_t base[2], uint32_t size[2]);
    bool create_strands ();
    uint32_t run (uint32_t max_nsteps);
    void swap_state ();
};
// ***** Begin synthesized operations *****

inline vec2 vload2 (const float *vp)
{
    return __extension__ (vec2){vp[0], vp[1]};
}
inline vec2 vcons2 (float r0, float r1)
{
    return __extension__ (vec2){r0, r1};
}
inline void vpack2 (tensor_2 &dst, vec2 v0)
{
    dst._data[0] = v0[0];
    dst._data[1] = v0[1];
}
inline vec2 vscale2 (float s, vec2 v)
{
    return __extension__ (vec2){s, s} * v;
}
inline float vdot2 (vec2 u, vec2 v)
{
    vec2 w = u * v;
    return w[0] + w[1];
}
// ***** End synthesized operations *****

typedef struct {
    int32_t gv_sz0;
    int32_t gv_sz1;
    float gv_width;
    tensor_2 gv_off;
    float gv_shear;
    float gv_angle;
    tensor_4 gv_parm;
} cmd_line_inputs;
static void init_defaults (cmd_line_inputs *inp)
{
    inp->gv_sz0 = 101;
    inp->gv_sz1 = 100;
    inp->gv_width = 0.1e1f;
    inp->gv_off[0] = 0.0f;
    inp->gv_off[1] = 0.0f;
    inp->gv_shear = 0.0f;
    inp->gv_angle = 0.0f;
    inp->gv_parm[0] = 0.0f;
    inp->gv_parm[1] = 0.0f;
    inp->gv_parm[2] = 0.0f;
    inp->gv_parm[3] = 0.0f;
}
static void register_inputs (cmd_line_inputs *inp, diderot::options< float, int32_t > *opts)
{
    opts->add("sz0", "# samples on faster axis", &inp->gv_sz0, true);
    opts->add("sz1", "# samples on slower axis", &inp->gv_sz1, true);
    opts->add("width", "approx width of world-space region sampled", &inp->gv_width, true);
    opts->add("off", "translation offset from origin-centered grid", 2, inp->gv_off._data, true);
    opts->add("shear", "amount of shear in sampling grid", &inp->gv_shear, true);
    opts->add("angle", "orientation (in degrees) of faster axis", &inp->gv_angle, true);
    opts->add("parm", "parameters that functions may use", 4, inp->gv_parm._data, true);
}
static bool init_inputs (world *wrld, cmd_line_inputs *inp)
{
    globals *glob = wrld->_globals;
    glob->gv_sz0 = inp->gv_sz0;
    glob->gv_sz1 = inp->gv_sz1;
    glob->gv_width = inp->gv_width;
    glob->gv_off = inp->gv_off;
    glob->gv_shear = inp->gv_shear;
    glob->gv_angle = inp->gv_angle;
    glob->gv_parm = inp->gv_parm;
    return false;
}
static std::string Outfile = "out";
static void register_outputs (diderot::options< float, int32_t > *opts)
{
    opts->add("o,output", "specify output-file file", &Outfile, true);
}
static bool init_globals (world *wrld)
{
    globals *glob = wrld->_globals;
    float l_op1_e3_l_4_2 = glob->gv_angle * 0.314159265358979323846264338328e1f / 0.180e3f;
    float l__t_3 = std::cos(l_op1_e3_l_4_2);
    float l__t_4 = std::sin(l_op1_e3_l_4_2);
    vec2 v_5 = vcons2(l__t_3, -l__t_4);
    vec2 v_6 = vcons2(l__t_4, l__t_3);
    float l__t_7 = static_cast<float>(glob->gv_sz0 - 1);
    float l__t_8 = static_cast<float>(glob->gv_sz1 - 1);
    vec2 v_9 = vcons2(glob->gv_width / l__t_7, glob->gv_width / l__t_8);
    vec2 v_10 = vcons2(v_9[0], 0.0f);
    vec2 v_11 = vcons2(vdot2(v_5, v_10), vdot2(v_6, v_10));
    vpack2(glob->gv_edge0, v_11);
    vec2 v_13 = vcons2(0.0f, v_9[1]);
    vec2 v_14 = vcons2(vdot2(v_5, v_13), vdot2(v_6, v_13)) + vscale2(glob->gv_shear, v_11);
    vpack2(glob->gv_edge1, v_14);
    vec2 v_16 = -(vscale2(l__t_7, v_11) + vscale2(l__t_8, v_14));
    float l_r_17 = 0.1e1f / 0.2e1f;
    vpack2(glob->gv_orig, vcons2(l_r_17 * v_16[0], l_r_17 * v_16[1]) + vload2(tensor_ref_2(glob->gv_off).addr(0)));
    return false;
}
static void sample_init (sample_strand *self, int32_t p_idx0_19, int32_t p_idx1_20)
{
    self->sv_out = 0.0f;
    self->sv_idx0 = p_idx0_19;
    self->sv_idx1 = p_idx1_20;
}
static diderot::strand_status sample_update (world *wrld, globals *glob, sample_strand *self)
{
    if (0 == self->sv_idx0) {
        if (0 == self->sv_idx1) {
            wrld->print() << "NRRD0004\n" << std::flush;
            wrld->print() << "# Complete NRRD file format specification at:\n" << std::flush;
            wrld->print() << "# http://teem.sourceforge.net/nrrd/format.html\n" << std::flush;
            wrld->print() << "type: float\n" << std::flush;
            wrld->print() << "dimension: 2\n" << std::flush;
            wrld->print() << "sizes: " << glob->gv_sz0 << " " << glob->gv_sz1 << "\n" << std::flush;
            wrld->print() << "kinds: space space\n" << std::flush;
            wrld->print() << "centers: cell cell\n" << std::flush;
            wrld->print() << "endian: little\n" << std::flush;
            wrld->print() << "encoding: raw\n" << std::flush;
            wrld->print() << "space dimension: 2\n" << std::flush;
            wrld->print() << "space directions: (" << vload2(tensor_ref_2(glob->gv_edge0).addr(0))[0] << "," << vload2(
                tensor_ref_2(glob->gv_edge0).addr(0))[1] << ") (" << vload2(tensor_ref_2(glob->gv_edge1).addr(0))[0] << "," << vload2(
                tensor_ref_2(glob->gv_edge1).addr(0))[1] << ")\n" << std::flush;
            wrld->print() << "space origin: (" << vload2(tensor_ref_2(glob->gv_orig).addr(0))[0] << "," << vload2(
                tensor_ref_2(glob->gv_orig).addr(0))[1] << ")\n" << std::flush;
            wrld->print() << "data file: out.nrrd\n" << std::flush;
            wrld->print() << "byte skip: -1\n" << std::flush;
        }
    }
    vec2 v_21 = vload2(tensor_ref_2(glob->gv_orig).addr(0)) + vscale2(static_cast<float>(self->sv_idx0),
        vload2(tensor_ref_2(glob->gv_edge0).addr(0))) + vscale2(static_cast<float>(self->sv_idx1),
        vload2(tensor_ref_2(glob->gv_edge1).addr(0)));
    self->sv_out = 0.1e1f - vdot2(v_21, v_21);
    return diderot::kStabilize;
}
bool output_get_out (world *wrld, Nrrd *nData)
{
    // Compute sizes of nrrd file
    size_t sizes[2];
    sizes[0] = wrld->_size[1];
    sizes[1] = wrld->_size[0];
    // Allocate nData nrrd
    if (nrrdMaybeAlloc_nva(nData, nrrdTypeFloat, 2, sizes) != 0) {
        char *msg = biffGetDone(NRRD);
        biffMsgAdd(wrld->_errors, msg);
        std::free(msg);
        return true;
    }
    // copy data to output nrrd
    char *cp = reinterpret_cast<char *>(nData->data);
    for (auto ix = wrld->_strands.begin_alive(); ix != wrld->_strands.end_alive(); ix = wrld->_strands.next_alive(ix)) {
        memcpy(cp, &wrld->_strands.strand(ix)->sv_out, 1 * sizeof(float));
        cp += 1 * sizeof(float);
    }
    nData->axis[0].kind = nrrdKindSpace;
    nData->axis[1].kind = nrrdKindSpace;
    return false;
}
static void write_output (world *wrld)
{
    Nrrd *nData;
    nData = nrrdNew();
    if (output_get_out(wrld, nData)) {
        std::cerr << "Error getting nrrd data:\n" << biffMsgStrGet(wrld->_errors) << std::endl;
        exit(1);
    }
    else if (nrrd_save_helper(Outfile, "", "nrrd", nData)) {
        exit(1);
    }
    nrrdNuke(nData);
}
/*---------- begin world-methods.in ----------*/
// Allocate the program's world
//
world::world ()
    : diderot::world_base (ProgramName, true, 2)
{
#ifndef DIDEROT_NO_GLOBALS
    this->_globals = new globals;
#endif

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    this->_tree = nullptr;
#endif
} // world constructor

// shutdown and deallocate the world
//
world::~world ()
{
#ifndef DIDEROT_NO_GLOBALS
    delete this->_globals;
#endif

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    delete this->_tree;
#endif

} // world destructor

// Initialize the program's world
//
bool world::init ()
{
    if (this->_stage != diderot::POST_NEW) {
        biffMsgAdd (this->_errors, "multiple calls to world::init");
        return true;
    }

#if !defined(DIDEROT_STANDALONE_EXEC) && !defined(DIDEROT_NO_INPUTS)
  // initialize the defined flags for the input globals
    init_defined_inputs (this);
#endif

    this->_stage = diderot::POST_INIT;

    return false;

}

// allocate the initial strands and initialize the rest of the world structure.
//
bool world::alloc (int32_t base[2], uint32_t size[2])
{
    size_t numStrands = 1;
    for (uint32_t i = 0;  i < 2;  i++) {
        numStrands *= size[i];
        this->_base[i] = base[i];
        this->_size[i] = size[i];
    }

    if (this->_verbose) {
        std::cerr << "world::alloc: " << size[0];
        for (uint32_t i = 1;  i < 2;  i++) {
            std::cerr << " x " << size[i];
        }
        std::cerr << std::endl;
    }

#ifdef DIDEROT_TARGET_PARALLEL
  // determine the block size based on the initial number of strands and the
  // number of workers
    this->_strands.set_block_size (this->_sched->_numWorkers, numStrands);
#endif

  // allocate the strand array
    if (this->_strands.alloc (numStrands)) {
        biffMsgAdd (this->_errors, "unable to allocate strand-state array\n");
        return true;
    }

  // initialize strand state pointers etc.
    this->_strands.create_strands (numStrands);

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    this->_tree = new diderot::kdtree<0, float, strand_array> (&this->_strands);
#endif

    return false;

} // world::alloc

// swap input and output states
//
inline void world::swap_state ()
{
    this->_strands.swap ();
}

#ifdef DIDEROT_HAS_KILL_ALL
void world::kill_all ()
{
    if (this->_strands.num_active() > 0) {
        for (auto ix = this->_strands.begin_active();
            ix != this->_strands.end_active();
            )
        {
            assert (this->_strands.status(ix) == diderot::kActive);
            ix = this->_strands.kill (ix);
        }
        this->_strands.finish_kill_all();
    }
    assert (this->_strands.num_active() == 0);
}
#endif

#ifdef DIDEROT_HAS_STABILIZE_ALL
void world::stabilize_all ()
{
#ifndef DIDEROT_NO_GLOBALS
    globals *glob = this->_globals;
#endif

    if (this->_strands.num_active() > 0) {
        for (auto ix = this->_strands.begin_active();
            ix != this->_strands.end_active();
            )
        {
            assert (this->_strands.status(ix) == diderot::kActive);
	    this->_strands._status[ix] = diderot::kStable;
            ix = this->_strands.strand_stabilize (ix);
        }
        this->_strands.finish_stabilize_all();
    }
    assert (this->_strands.num_active() == 0);
}
#endif
/*---------- end world-methods.in ----------*/

bool world::create_strands ()
{
    if (init_globals(this)) {
        return true;
    }
    globals *glob = this->_globals;
    int lo_0 = 0;
    int hi_1 = glob->gv_sz1 - 1;
    int lo_2 = 0;
    int hi_3 = glob->gv_sz0 - 1;
    int32_t base[2] = {lo_0,lo_2,};
    uint32_t size[2] = {static_cast<uint32_t>(hi_1 - lo_0 + 1),static_cast<uint32_t>(hi_3 - lo_2 + 1),};
    if (this->alloc(base, size)) {
        return true;
    }
    uint32_t ix = 0;
    for (int i_idx1_22 = lo_0; i_idx1_22 <= hi_1; i_idx1_22++) {
        for (int i_idx0_23 = lo_2; i_idx0_23 <= hi_3; i_idx0_23++) {
            sample_init(this->_strands.strand(ix), i_idx0_23, i_idx1_22);
            ++ix;
        }
    }
    this->swap_state();
    this->_stage = diderot::POST_CREATE;
    return false;
}
/*---------- begin seq-run-nobsp.in ----------*/
//! Run the Diderot program (sequential version without BSP semantics)
//! \param max_nsteps the limit on the number of super steps; 0 means unlimited
//! \return the number of steps taken, or 0 on error.
uint32_t world::run (uint32_t max_nsteps)
{
    if (this->_stage < diderot::POST_CREATE) {
        biffMsgAdd (this->_errors, "attempt to run uninitialized program\n");
        return 0;
    }
    else if (this->_stage == diderot::DONE) {
        return 0;
    }
    else if (this->_stage == diderot::POST_CREATE) {
#ifdef DIDEROT_HAS_GLOBAL_START
        this->global_start();
#endif
        this->_stage = diderot::RUNNING;
    }
    assert (this->_stage == diderot::RUNNING);

#ifndef DIDEROT_NO_GLOBALS
    globals *glob = this->_globals;
#endif

    if (max_nsteps == 0) {
        max_nsteps = 0xffffffff;  // essentially unlimited
    }

    double t0 = airTime();

    if (this->_verbose) {
        std::cerr << "run with " << this->_strands.num_alive() << " strands ..." << std::endl;
    }

#ifdef DIDEROT_HAS_START_METHOD
    this->run_start_methods();
#endif

  // iterate until all strands are stable
    uint32_t maxSteps = 0;
    for (auto ix = this->_strands.begin_active();
         ix != this->_strands.end_active();
         )
    {
        diderot::strand_status sts = this->_strands.status(ix);
        uint32_t nSteps = 0;
        while ((! sts) && (nSteps < max_nsteps)) {
            nSteps++;
            sts = this->_strands.strand_update(this, glob, ix);
        }
        switch (sts) {
          case diderot::kStabilize:
          // stabilize the strand's state.
            ix = this->_strands.strand_stabilize (ix);
            break;
#ifdef DIDEROT_HAS_STRAND_DIE
          case diderot::kDie:
            ix = this->_strands.kill (ix);
            break;
#endif
          default:
            assert (sts == this->_strands.status(ix));
	    ix = this->_strands.next_active(ix);
            break;
        }
        if (maxSteps < nSteps) maxSteps = nSteps;
    }

    this->_run_time += airTime() - t0;

    if (this->_strands.num_active() == 0)
        this->_stage = diderot::DONE;

    return maxSteps;

} // world::run
/*---------- end seq-run-nobsp.in ----------*/

/*---------- begin namespace-close.in ----------*/

} // namespace Diderot
/*---------- end namespace-close.in ----------*/

/*---------- begin seq-main.in ----------*/
using namespace Diderot;

//! Main function for standalone sequential C target
//
int main (int argc, const char **argv)
{
    bool        timingFlg = false;      //! true if timing computation
    uint32_t    stepLimit = 0;          //! limit on number of execution steps (0 means unlimited)
    std::string printFile = "-";        //! file to direct printed output into
#ifdef DIDEROT_EXEC_SNAPSHOT
    uint32_t    snapshotPeriod = 0;     //! supersteps per snapshot; 0 means no snapshots
#endif
    uint32_t    nSteps = 0;             //! number of supersteps taken

  // create the world
    world *wrld = new (std::nothrow) world();
    if (wrld == nullptr) {
        std::cerr << "unable to create world" << std::endl;
        exit (1);
    }

#ifndef DIDEROT_NO_INPUTS
  // initialize the default values for the inputs
    cmd_line_inputs inputs;
    init_defaults (&inputs);
#endif

  // handle command-line options
    {
        diderot::options<float,int32_t> *opts = new diderot::options<float,int32_t> ();
        opts->add ("l,limit", "specify limit on number of super-steps (0 means unlimited)",
            &stepLimit, true);
#ifdef DIDEROT_EXEC_SNAPSHOT
        opts->add ("s,snapshot",
            "specify number of super-steps per snapshot (0 means no snapshots)",
            &snapshotPeriod, true);
#endif
        opts->add ("print", "specify where to direct printed output", &printFile, true);
        opts->addFlag ("v,verbose", "enable runtime-system messages", &(wrld->_verbose));
        opts->addFlag ("t,timing", "enable execution timing", &timingFlg);
#ifndef DIDEROT_NO_INPUTS
      // register options for setting global inputs
        register_inputs (&inputs, opts);
#endif
        register_outputs (opts);
        opts->process (argc, argv);
        delete opts;
    }

  // redirect printing (if necessary)
    if (printFile.compare("-") != 0) {
        wrld->_printTo = new std::ofstream (printFile);
        if (wrld->_printTo->fail()) {
            std::cerr << "Error opening print file" << std::endl;
            exit(1);
        }
    }

  // initialize scheduler stuff
    if (wrld->_verbose) {
        std::cerr << "initializing world ..." << std::endl;
    }
    if (wrld->init()) {
        std::cerr << "Error initializing world:\n" << wrld->get_errors() << std::endl;
        exit(1);
    }

#ifndef DIDEROT_NO_INPUTS
  // initialize the input globals
    if (init_inputs (wrld, &inputs)) {
        std::cerr << "Error initializing inputs:\n" << wrld->get_errors() << std::endl;
        exit(1);
    }
#endif

  // run the generated global initialization code
    if (wrld->_verbose) {
        std::cerr << "initializing globals and creating strands ...\n";
    }
    if (wrld->create_strands()) {
        std::cerr << "Error in global initialization:\n"
            << wrld->get_errors() << std::endl;
        exit(1);
    }

#ifdef DIDEROT_EXEC_SNAPSHOT

    if (snapshotPeriod > 0) {
     // write initial state as snapshot 0
        write_snapshot (wrld, "-0000");
     // run the program for `snapshotPeriod` steps at a time with a snapshot after each run
        while (true) {
            uint32_t n, limit;
          // determine a step limit for the next run
            if (stepLimit > 0) {
                if (stepLimit <= nSteps) {
                    break;
                }
                limit = std::min(stepLimit - nSteps, snapshotPeriod);
            }
            else {
                limit = snapshotPeriod;
            }
          // run the program for upto limit steps
            if ((n = wrld->run (limit)) == 0) {
                break;
            }
            nSteps += n;
            if ((wrld->_errors->errNum > 0) || (wrld->_strands.num_alive() == 0)) {
                break;
            }
          // write a snapshot with the step count as a suffix
            std::string suffix = std::to_string(nSteps);
            if (suffix.length() < 4) {
                suffix = std::string("0000").substr(0, 4 - suffix.length()) + suffix;
            }
            suffix = "-" + suffix;
            write_snapshot (wrld, suffix);
        }
    }
    else {
        nSteps = wrld->run (stepLimit);
    }

#else // !DIDEROT_EXEC_SNAPSHOT

    nSteps = wrld->run (stepLimit);

#endif // DIDEROT_EXEC_SNAPSHOT

    if (wrld->_errors->errNum > 0) {
        std::cerr << "Error during execution:\n" << wrld->get_errors() << std::endl;
        exit(1);
    }

    if ((stepLimit != 0) && (wrld->_strands.num_active() > 0)) {
#ifdef DIDEROT_STRAND_ARRAY
        if (wrld->_verbose) {
            std::cerr << "Step limit expired; "
                << wrld->_strands.num_active() << " active strands remaining" << std::endl;
        }
#else
      // step limit expired, so kill remaining strands
        if (wrld->_verbose) {
            std::cerr << "Step limit expired. Killing remaining "
                << wrld->_strands.num_active() << " active strands" << std::endl;
        }
        wrld->kill_all();
#endif
    }

    if (wrld->_verbose) {
        std::cerr << "done: " << nSteps << " steps, in " << wrld->_run_time << " seconds"
            << std::endl;
    }
    else if (timingFlg) {
        std::cout << "usr=" << wrld->_run_time << std::endl;
    }

  // output the final strand states
    write_output (wrld);

    delete wrld;

    return 0;

} // main
/*---------- end seq-main.in ----------*/

